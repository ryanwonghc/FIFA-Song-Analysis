import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

df = pd.read_csv('Notebooks/fifa_spotify_data_cleaned')

# ------------------------------- Cleaning -------------------------------
df['album_release_date'] = df['album_release_date'].astype('datetime64')
df = df.fillna('None')
df['playlist_year'] = df.playlist_name.apply(lambda x: int(x[5:7])) # Create playlist year column

# ------------------------------- Dash App -------------------------------
app = dash.Dash(__name__)
server = app.server

# --------------------------------- HTML ---------------------------------
app.layout = html.Div([

    html.H1('FIFA Playlist Data Visualization', style = {'text-align': 'center'}),
    html.Br(),

    html.H2('Audio Features', style = {'text-align': 'center'}),

    dcc.Dropdown(id="selected_audio_feature",
                 options=[
                     {'label': 'Acousticness', 'value': 'acousticness'},
                     {'label': 'Danceability', 'value': 'danceability'},
                     {'label': 'Energy', 'value': 'energy'},
                     {'label': 'Instrumentalness', 'value': 'instrumentalness'},
                     {'label': 'Key', 'value': 'key'},
                     {'label': 'Loudness', 'value': 'loudness'},
                     {'label': 'Mode', 'value': 'mode'},
                     {'label': 'Tempo', 'value': 'tempo'},
                     {'label': 'Valence', 'value': 'valence'}],
                 multi=False,
                 value='acousticness',
                 style={'width': "75%", 'diplay': 'inline-block'}
                 ),

    dcc.Graph(id='aud_vs_year_lineplot', figure={}),
    html.Br(),

    dcc.Dropdown(id="selected_year",
                 options=[
                     {'label': 'FIFA 2020', 'value': 20},
                     {'label': 'FIFA 2019', 'value': 19},
                     {'label': 'FIFA 2018', 'value': 18},
                     {'label': 'FIFA 2017', 'value': 17},
                     {'label': 'FIFA 2016', 'value': 16},
                     {'label': 'FIFA 2015', 'value': 15},
                     {'label': 'FIFA 2014', 'value': 14}],
                 multi=False,
                 value=20,
                 style={'width': "75%", 'diplay': 'inline-block'}
                 ),

    dcc.Graph(id='aud_dist_boxplot', figure={}),
    html.Br(),

    dcc.Graph(id='track_artist_popularity', figure= px.scatter(
                                            data_frame = df,
                                            x = df.avg_artist_popularity,
                                            y = df.track_popularity,
                                            color = df.playlist_name,
                                            title = 'Track vs. Artist Popularity',
                                            hover_data = ['track_name','artist1_name', 'artist2_name', 'artist3_name']
                                        )),
    html.Br(),

    dcc.Graph(id='track_album_popularity', figure= px.scatter(
                                            data_frame = df[df.single == 0],
                                            x = df[df.single == 0].album_popularity,
                                            y = df[df.single == 0].track_popularity,
                                            color = df[df.single == 0].playlist_name,
                                            title = 'Track vs. Album Popularity',
                                            hover_data = ['track_name','album_name']
                                        ))


])

# ------------------------------- Callbacks -------------------------------
@app.callback(
    Output(component_id='aud_vs_year_lineplot', component_property='figure'),
    [Input(component_id='selected_audio_feature', component_property='value')]
)

def update_graph(selected_audio_feature):

    filtered_df = df.copy()
    filtered_df = filtered_df.groupby(['playlist_year']).mean()

    # Plotly Express
    fig = px.line(
        data_frame = filtered_df,
        x = filtered_df.index,
        y = filtered_df[selected_audio_feature],
        title = 'Audio Feature vs. Year'
    )

    return fig

@app.callback(
    Output(component_id='aud_dist_boxplot', component_property='figure'),
    [Input(component_id='selected_year', component_property='value')]
)

def update_graph(selected_year):

    filtered_df = df.copy()
    filtered_df = filtered_df[filtered_df.playlist_year == selected_year]

    fig = make_subplots(rows=1, cols=9, subplot_titles=("Acousticness", "Danceability", "Energy", "Instrumentalness",
                                                        "Key", "Loudness", "Mode", "Tempo", "Valence"))

    fig.add_trace(
        go.Box(y=filtered_df.acousticness, boxmean=True),
        row=1, col=1
    )
    fig.add_trace(
        go.Box(y=filtered_df.danceability, boxmean=True),
        row=1, col=2
    )
    fig.add_trace(
        go.Box(y=filtered_df.energy, boxmean=True),
        row=1, col=3
    )
    fig.add_trace(
        go.Box(y=filtered_df.instrumentalness, boxmean=True),
        row=1, col=4
    )
    fig.add_trace(
        go.Box(y=filtered_df.key, boxmean=True),
        row=1, col=5
    )
    fig.add_trace(
        go.Box(y=filtered_df.loudness, boxmean=True),
        row=1, col=6
    )
    fig.add_trace(
        go.Box(y=filtered_df['mode'], boxmean=True),
        row=1, col=7
    )
    fig.add_trace(
        go.Box(y=filtered_df.tempo, boxmean=True),
        row=1, col=8
    )
    fig.add_trace(
        go.Box(y=filtered_df.valence, boxmean=True),
        row=1, col=9
    )

    fig.update_layout(height=400, width=1500,
                      title_text="Distribution of Audio Features in the FIFA 20{} Playlist".format(selected_year))

    return fig

# --------------------------------- Main ---------------------------------
if __name__=='__main__':
    app.run_server(debug=True)

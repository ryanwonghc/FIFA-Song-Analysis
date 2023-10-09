import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import pandas as pd
import json
import time


def extract_song_data(sp, playlist_uri, playlist_name):
    '''
    Pulls song, song audio, album, and song artist data via spotify object
    :param sp: Spotipy object allowing for access to Spotify data
    :param playlist_uri: playlist URI from spotify
    :return: dataframe containing song and song audio information from all songs in playlist
    '''
    if sp is None or playlist_uri is None:
        return None
    
    print(sp, playlist_uri, playlist_name)
    
    result_df = pd.DataFrame()
    for song in sp.playlist_tracks(playlist_uri)["items"]:
        print("yes")
        # store all relevant information about a song in a dict, to add to pandas df
        new_song_data = {}
        new_song_data["playlist"] = playlist_name

        # Song Basic Info
        song_uri = song["track"]["uri"].split(":")[2]
        print(song_uri)
        song_data = sp.track(song_uri)
        print(song_data)
        for field in ["name","popularity","duration_ms","explicit"]:
            new_song_data["song_"+field] = song_data[field]
        print(new_song_data["song_name"])

        # Song Audio Info
        audio_data = sp.audio_features([song_uri])[0]
        for field in ["danceability","energy","key","loudness","mode","speechiness",
                      "acousticness","instrumentalness","liveness","valence","tempo",
                      "time_signature"]:
            new_song_data["audio_"+field] = audio_data[field]

        # Album Info
        album_uri = song["track"]["album"]["uri"]
        print(album_uri)
        album_data = sp.album(album_uri)
        for field in ["name","release_date","total_tracks","popularity"]:
            new_song_data["album_"+field] = album_data[field]
        
        # Artist Info (only for the first artist listed on the track)
        artist_uri = song["track"]["artists"][0]["uri"]
        print(artist_uri)
        artist_data = sp.artist(artist_uri)
        for field in ["name","popularity","genres","followers"]:
            if field == "followers":
                new_song_data["artist_"+field] = artist_data[field]["total"]
            else:
                new_song_data["artist_"+field] = artist_data[field]

        new_song_data_df = pd.DataFrame(new_song_data)
        result_df = pd.concat([result_df, new_song_data_df], ignore_index=True)

        time.sleep(3)
    
    return result_df


def one_hot_encoding(df, column):
    '''
    :param df: dataframe containing column you wish to one hot encode
    :param column: name of column that you wish to one hot encode
    :return: dataframe with target column one hot encoded
    '''
    # perform one hot encoding and join to original dataframe
    one_hot = pd.get_dummies(df[column],prefix='genre')
    df = df.drop(column, axis=1)
    groupby_columns = df.columns.values.tolist()
    df = df.join(one_hot)

    # aggregate song genres to one row
    df = df.groupby(groupby_columns).sum().reset_index()
    return df

if __name__ == "__main__":
    # URIs for the last 11 FIFA soundtrack playlists on Spotify
    playlists = {
        'FIFA24':'37i9dQZF1DX3rXtgePifMs',
        'FIFA23':'37i9dQZF1DX4vgOVqe6BJn',
        'FIFA22':'2a6OSlFchVcDonrXMMJ6EM',
        'FIFA21':'3EEtqDscUeqwVVdx6JuMKU',
        'FIFA20':'0rkxErbruAmcxwdLL6ZCz8',
        'FIFA19':'5wTJTZkGb30JuYYfz7vbDL',
        'FIFA18':'1Vj65Ch6pO2mnZbgm2dn07',
        'FIFA17':'4zZveHJxa685kuS2IxlVOY',
        'FIFA16':'03lUYFsfkESxG71B2dYosj',
        'FIFA15':'00i82lDzMDdiHWNjrIGAyw',
        'FIFA14':'6uhKIwBpVEX9loDnk4iOcM'
    }

    spotify_client_credentials = SpotifyClientCredentials(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = spotify_client_credentials)

    song_data_agg = pd.DataFrame()
    for name, uri in playlists.items():
        print(name)
        song_data = extract_song_data(sp, uri, name)
        song_data_agg = pd.concat([song_data_agg,song_data],ignore_index=True)
    
    genre_one_hot = one_hot_encoding(song_data_agg, 'artist_genres')
    genre_one_hot.to_csv('data/fifa_playlist_song_data2.csv',index=False)
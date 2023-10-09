import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import pandas as pd
import json


spotify_client_credentials = SpotifyClientCredentials(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = spotify_client_credentials)

print(sp.tracks(['2cSdAkzAf2T4j4aLvx4LLz']))
import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import os
from spotipy import util
from utils.spotify_util import SpotifyAPI
import asyncio
from google.cloud import secretmanager

secrets = ['SPOTIPY_CLIENT_ID', 'SPOTIFY_CLIENT_SECRET', 'SPOTIFY_REDIRECT_URI']



os.environ['SPOTIFY_CLIENT_ID'] = 'id'
os.environ['SPOTIFY_CLIENT_SECRET'] = 'id'
os.environ['SPOTIFY_REDIRECT_URI'] = 'id'
if __name__ == "__main__":
    sp = SpotifyAPI()
    results = sp.get_top_songs()
    st.write(results)




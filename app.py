import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import os
from spotipy import util
from utils.spotify_util import SpotifyAPI
import asyncio




if __name__ == "__main__":
    sp = SpotifyAPI()
    results = sp.get_top_songs()
    st.write(results)




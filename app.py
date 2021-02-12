import streamlit as st
from utils.spotify_util import SpotifyAPI



if __name__ == "__main__" :
    sp = SpotifyAPI()
    sp.set_all_env_variables()
    results = sp.get_saved_songs()
    st.write(results)




import streamlit as st
from utils.spotify_util import SpotifyUtil



if __name__ == "__main__" :
    sp = SpotifyUtil()
    sp.set_all_env_variables()
    results = sp.get_saved_tracks()
    st.write(results)




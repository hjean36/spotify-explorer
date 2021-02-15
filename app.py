import streamlit as st
from utils.spotify_util import SpotifyUtil



if __name__ == "__main__" :
    sp = SpotifyUtil()
    env_variables_set = sp.set_all_env_variables()
    st.write('Saved Tracks')
    st.write(str(env_variables_set))
    results = sp.get_saved_tracks()
    st.write(results)




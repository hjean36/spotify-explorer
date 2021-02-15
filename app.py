import streamlit as st
from utils.spotify_util import SpotifyUtil



if __name__ == "__main__" :
    def _process_tracks(self, item):
        track = item['track']
        track_name = track['album']['name']
        track_artist_name = track['artists'][0]['name']
        return f"{track_name} - {track_artist_name}"

    sp = SpotifyUtil()
    env_variables_set = sp.set_all_env_variables()
    st.write('Saved Tracks')
    st.write(str(env_variables_set))
    sp = sp.generate_auth_sp('user-library-read')
    if sp:
        st.write('Authenticated Spotify')
    results = sp.current_user_saved_tracks(limit=10)
    if results:
        st.write('Retrieved Tracks')
    songs = [_process_tracks(item) for item in results['items']]
    if songs:
        st.write("Songs Processed")
    st.write(songs)




from utils.spotify import SpotifyAPI
import streamlit as st


class SpotifyUtil(SpotifyAPI):

    def _process_tracks(self, item):
        track = item['track']
        track_name = track['album']['name']
        track_artist_name = track['artists'][0]['name']
        return f"{track_name} - {track_artist_name}"

    @st.cache
    def get_saved_tracks(self):
        sp = self.generate_auth_sp('user-library-read')
        results = sp.current_user_saved_tracks(limit=10)
        songs = [self._process_tracks(item) for item in results['items']]
        return songs

    @st.cache(suppress_st_warning=True)
    def get_top_tracks(self, time_range, limit):
        sp = self.generate_auth_sp('user-top-read')
        results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
        songs = [self._process_tracks(item) for item in results['items']]
        return songs

    @st.cache(suppress_st_warning=True)
    def get_top_tracks_uris(self, items, time_range, limit):
        sp = self.generate_auth_sp('user-top-read')
        results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
        song_uris = [item['track']['uri'] for item in results['item']]
        return song_uris

    @st.cache(suppress_st_warning=True)
    def get_audio_features(self, song_uris):
        sp = self.generate_auth_sp('user-top-read')
        audio_features = sp.audio_features(song_uris)
        return audio_features

    @st.cache(suppress_st_warning=True)
    def get_audio_analysis(self, song_uris):
        sp = self.generate_auth_sp('user-top-read')
        audio_analysis = [sp.audio_features(uri) for uri in song_uris]
        return audio_analysis

    @st.cache(suppress_st_warning=True)
    def recommend_songs(self):
        sp = self.generate_auth_sp('user-library-read')
        results = self.current_user_top_artists(time_range=range, limit=10)
        artists_uris = [results['items'][x]['uri'] for x in range(results['limit'])]
        songs = [sp.recommendations(seed_artists=uri) for uri in artists_uris]
        return songs


if __name__ == '__main__':
    SpotifyUtil

from utils.spotify import SpotifyAPI
from contextlib import redirect_stdout
import background
import asyncio
import sys
import tekore as tk


class SpotifyUtil(SpotifyAPI):

    def _process_tracks(self, item):
        track = item['track']
        track_name = track['album']['name']
        track_artist_name = track['artists'][0]['name']
        return f"{track_name} - {track_artist_name}"

    def get_saved_tracks(self):
        sp = self.generate_auth_sp('user-library-read')
        results = sp.current_user_saved_tracks()
        songs = [self._process_tracks(item) for item in results['items']]
        return songs

    def get_top_tracks(self, time_range, limit):
        sp = self.generate_auth_sp('user-top-read')
        results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
        songs = [self._process_tracks(item) for item in results['items']]
        return songs

    def get_top_tracks_uris(self, items, time_range, limit):
        sp = self.generate_auth_sp('user-top-read')
        results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
        song_uris = [item['track']['uri'] for item in results['item']]
        return song_uris

    def get_top_artists_uris(self, items, time_range, limit):
        sp = self.generate_auth_sp('user_top_read')
        results = sp.current_user_top_artists(limit=limit, time_range=time_range)
        songs_uris = []

    def get_audio_features(self, song_uris):
        sp = self.generate_auth_sp('user-top-read')
        audio_features = sp.audio_features(song_uris)
        return audio_features

    def get_audio_analysis(self, song_uris):
        sp = self.generate_auth_sp('user-top-read')
        audio_analysis = [sp.audio_features(uri) for uri in song_uris]
        return audio_analysis

    def recommend_songs(self, artists_uris):
        sp = self.generate_auth_sp('user-library-read')
        results = self.current_user_top_artists(time_range=range, limit=10)
        artists_uris = [results['items'][x]['uri'] for x in range(results['limit'])]
        songs = [sp.recommendations(seed_artists=uri) for uri in artists_uris]
        return songs


if __name__ == '__main__':
    SpotifyUtil

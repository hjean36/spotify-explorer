"""This util wraps around the spotify API and provides an interface for making calls via the python librabry """
import os
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyPKCE

os.environ['SPOTIPY_CLIENT_ID'] = config("SPOTIPY_CLIENT_ID")
os.environ['SPOTIPY_CLIENT_SECRET'] = config("SPOTIPY_CLIENT_SECRET")
os.environ['SPOTIPY_REDIRECT_URI'] = config("SPOTIPY_REDIRECT_URI")
class SpotifyAPI:

    def generate_auth(self, scope):
        auth_manger = spotipy.SpotifyOAuth(
            client_id=config('SPOTIPY_CLIENT_ID'),
            client_secret=config('SPOTIPY_CLIENT_SECRET'),
            redirect_uri=config('SPOTIPY_REDIRECT_URI'),
            scope=scope,
            open_browser=True

        )
        return auth_manger

    def get_top_songs(self):
        auth_manager = self.generate_auth("user-library-read")
        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.current_user_saved_tracks()
        songs = []
        for idx, item in enumerate(results['items']):
            track = item['track']
            song = [f"{idx} {track['artists'][0]['name']} {track['name']}"]
            songs.extend(song)
        return songs

    def get_song(self):
        raise NotImplementedError()

    def update_playlist(self):
        raise NotImplementedError()

    def get_song_seeds(self):
        raise NotImplementedError()

    def get_recommendation(self):
        raise NotImplementedError()

    def get_artist(self):
        raise NotImplementedError()


if __name__ == '__main__':
    SpotifyAPI

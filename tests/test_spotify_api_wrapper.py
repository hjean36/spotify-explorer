import unittest
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import os
from utils.spotify import SpotifyAPI


os.environ['SPOTIPY_CLIENT_ID'] = config("SPOTIPY_CLIENT_ID")
os.environ['SPOTIPY_CLIENT_SECRET'] = config("SPOTIPY_CLIENT_SECRET")
os.environ['SPOTIPY_REDIRECT_URI'] = config("SPOTIPY_REDIRECT_URI")

class TestSpotifyAPI(unittest.TestCase):

    def test_get_key(self):
        sp = SpotifyAPI()
        client_id = sp.get_secret("SPOTIPY_CLIENT_ID")
        self.assertIsNotNone(client_id)

    def test_get_history(self):
        self.skipTest("")

    def test_get_songs(self):
        sp = SpotifyAPI()
        songs = sp.get_top_songs()
        print(songs)

    def test_add_to_playlist(self):
        self.skipTest("")

    def test_generate_recomm(self):
        self.skipTest("")

    def test_get_song_seeds(self):
        self.skipTest("")

    def test_get_artists(self):
        self.skipTest("")

    def test_create_playlist(self):
        self.skipTest("")


if __name__ == '__main__':
    unittest.main()

"""This util wraps around the spotify API and provides an interface for making calls via the python librabry """
import os
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyPKCE
from google.cloud import secretmanager
from decouple import config
import requests


def process_songs(results):
    songs = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        song = [f"{idx} {track['artists'][0]['name']} - {track['name']}"]
        songs.extend(song)
    return songs


class SpotifyAPI:
    def __init__(self):
        self.secrets = [
                    'SPOTIPY_CLIENT_ID',
                    'SPOTIPY_CLIENT_SECRET',
                    'SPOTIPY_REDIRECT_URI'
                    ]

    def get_secret(self, secret_id, project_id='spotify-explore', version_id='latest'):
        client = secretmanager.SecretManagerServiceClient()
        secret_detail = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
        response = client.access_secret_version(request={"name": secret_detail})
        data = response.payload.data.decode("UTF-8")
        return data

    def set_all_env_variables(self):
        for s in self.secrets:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config("GOOGLE_APPLICATION_CREDENTIALS")
            os.environ[s] = self.get_secret(secret_id=s)

    def generate_auth_sp(self, scope):
        auth_manager = spotipy.SpotifyOAuth(
            scope=scope,
            open_browser=True
        )
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return sp

if __name__ == '__main__':
    SpotifyAPI()

"""This util wraps around the spotify API and provides an interface for making calls via the python librabry """
import os
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyPKCE
from google.cloud import secretmanager
from decouple import config
import requests


class SpotifyAPI:
    def __init__(self):
        self.secrets = [
            'SPOTIPY_CLIENT_ID',
            'SPOTIPY_CLIENT_SECRET',
            'SPOTIPY_REDIRECT_URI'
        ]

    @staticmethod
    def get_secret(secret_id, project_id='spotify-explore', version_id='latest'):
        client = secretmanager.SecretManagerServiceClient()
        secret_detail = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
        response = client.access_secret_version(request={"name": secret_detail})
        data = response.payload.data.decode("UTF-8")
        return data

    @staticmethod
    def generate_auth_sp(scope):
        auth_manager = spotipy.SpotifyOAuth(
            scope=scope,
            open_browser=True
        )
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return sp

    def set_all_env_variables(self):
        for s in self.secrets:
            try:
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config("GOOGLE_APPLICATION_CREDENTIALS")
            except Exception as e:
                print('Auth using Google Cloud Default')
            os.environ[s] = self.get_secret(secret_id=s)


if __name__ == '__main__':
    SpotifyAPI()

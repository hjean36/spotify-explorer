"""This util wraps around the spotify API and provides an interface for making calls via the python librabry """
import os
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyPKCE
from google.cloud import secretmanager

os.environ['SPOTIPY_CLIENT_ID'] = 'SPOTIPY_CLIENT_ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = "SPOTIPY_CLIENT_SECRET"
os.environ['SPOTIPY_REDIRECT_URI'] = "SPOTIPY_REDIRECT_URI"

class SpotifyAPI:

    def get_secret(self, secret_id, project_id='spotify explore', version_id='latest'):
        client = secretmanager.SecretManagerServiceClient()
        secret_detail = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
        response = client.access_secret_version(request={"name": secret_detail})
        data = response.payload.data.decode("UTF-8")
        return data

    def set_all_env_variables(self, variables: list):
        for v in variables:
            os.environ[v] = self.get_secret(secret_id=v)

    def generate_auth(self, scope):
        auth_manger = spotipy.SpotifyOAuth(
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
    SpotifyAPI()

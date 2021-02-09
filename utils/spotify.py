"""This util wraps around the spotify API and provides an interface for making calls via the python librabry """


class SpotifyAPI:
    def __init__(self, client, auth_options):
        client = client
        auth_options

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

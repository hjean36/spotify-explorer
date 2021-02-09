from utils.spotify import SpotifyAPI


class SpotifyUtil(SpotifyAPI):

    def __init__(self, users, songs=[], options=[]):
        self.users = users
        self.songs = songs
        self.options = options

    def get_user_history(self, user):
        raise NotImplementedError()

    def get_top_genres(self, user):
        raise NotImplementedError()

    def get_top_artists(self, user):
        raise NotImplementedError()

    def recommend_song(self):
        raise NotImplementedError()

    def recommend_artist(self):
        raise NotImplementedError()

    def create_recommended_playlist(self, user):
        raise NotImplementedError()


if __name__ == '__main__':
    SpotifyUtil
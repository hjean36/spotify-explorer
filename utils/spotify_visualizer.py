from utils.spotify_util import SpotifyUtil

class SpotifyVisualizer(SpotifyUtil):
    def __init__(self, options):
        self.options = options

    def generate_overview_chart(self):
        raise NotImplementedError()

    def generate_top_genres_chart(self):
        raise NotImplementedError()

if __name__ == '__main__':
    SpotifyVisualizer
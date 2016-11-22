class Movie():
    """
    This class keeps information about a movie.
    Parameters
    ----------
    title: str, movie's title
    poster_image_url: str, url of a poster image
    trailer_youtube_url: str, a trailer url at YouTube
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

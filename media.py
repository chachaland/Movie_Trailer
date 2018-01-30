import webbrowser


class Movie(object):
    """Class providing a way to store movie related information

        Args:
                movie_title (str): Title of a movie
                movie_storyline (str): Storyline of a movie
                poster_image (str): url of a poster image of a movie
                trailer_youtube_url (str): url of a movie trailer

        Attributes:
                movie_title (str): Title of a movie
                movie_storyline (str): Storyline of a movie
                poster_image (str): url of a poster image of a movie
                trailer_youtube_url (str): url of a movie trailer

        Methods:
                show_trailer: opening a trailer from the web
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open a trailer from the web"""
        webbrowser.open(self.trailer_youtube_url)

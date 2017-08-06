""" This module implements the Movie class """


class Movie(object):
    """ Movie class encapsulate movie_title, movie_poster_image_url,
    and movie_trailer_youtube_url properties
    """

    def __init__(self, movie_title, movie_poster_image_url,
                 movie_trailer_youtube_url):
        """ The Movie class constructor initializes all the properties """

        # Movie title property
        self.title = movie_title

        # Movie poster image URL property
        self.poster_image_url = movie_poster_image_url

        # Movie trailer youtube URL
        self.trailer_youtube_url = movie_trailer_youtube_url

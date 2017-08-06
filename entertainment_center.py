""" This module display a website that contains poster images that when
clicked plays a youtube trailer.
"""

import media
import fresh_tomatoes


def get_movie_list():
    """ This function creates a list of Movie objects and return it. """

    # create number of movie objects
    title = "emoji movie"
    movie_poster_image_url = "images/Emoji-movie-poster.jpg"
    movie_trailer_youtube_url = "https://www.youtube.com/watch?v=o_nfdzMhmrA"
    mv1 = media.Movie(title, movie_poster_image_url, movie_trailer_youtube_url)

    title = "The Lion King"
    movie_poster_image_url = "images/Lion-king-poster.jpg"
    movie_trailer_youtube_url = "https://www.youtube.com/watch?v=4sj1MT05lAA"
    mv2 = media.Movie(title, movie_poster_image_url, movie_trailer_youtube_url)

    title = "Popeye"
    movie_poster_image_url = "images/Popeye-poster.jpg"
    movie_trailer_youtube_url = "https://www.youtube.com/watch?v=i4tNuM9XttM"
    mv3 = media.Movie(title, movie_poster_image_url, movie_trailer_youtube_url)

    title = "Rango"
    movie_poster_image_url = "images/Rango-poster.jpg"
    movie_trailer_youtube_url = "https://www.youtube.com/watch?v=rHm5-av1Uks"
    mv4 = media.Movie(title, movie_poster_image_url, movie_trailer_youtube_url)

    # creates a list of Movie objects
    return [mv1, mv2, mv3, mv4]

# create the HTML web page and open the browser to display the website
fresh_tomatoes.open_movies_page(get_movie_list())

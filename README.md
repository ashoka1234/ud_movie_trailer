# Movie-trailer

Movie-trailer is a web site that allows movie trailer playback when a movie poster image is clicked. The movie poster images are shown on the web site.

Install
-------
The website HTML file `fresh_tomatoes.html` is created by a backend written in Python and saved in the project directory.  The poster images are stored in the subdirectory `images`. The backend consists of three Python files:

`entertainment_center.py :` Creates a list of movie objects and calls open_movies_page() function which needs the list of movie objects as input in order to build the HTML file, so you can display your website.

`fresh_tomatoes.py :` This module implements a function called open_movies_page that takes in one argument, which is a list of movies, and creates an HTML file which will display all of your favorite movies. It further opens a browser in order to display the webpage created.

`media.py :` This module implements the movie class.

Run
---
Run the Python module `entertainment_center.py` in order to create the web page `fresh_tomatoes.html`. Open this file to display the movie trailer website.

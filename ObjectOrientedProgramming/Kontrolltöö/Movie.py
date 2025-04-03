class Movie:
    """
    Represent a movie model.
    """

    def __init__(self, movie_name, year):
        """Movie constructor."""
        self.movie_name = movie_name
        self.year = year
        self.movies = []
        self.movie_viewings = []

    def __repr__(self):
        """Represent movie."""
        return f"Movie(name={self.movie_name}, genre={self.movie_genre}, year={self.year})"

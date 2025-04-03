from typing import Any

import Movie

class Thriller:
    """Represent a thriller model"""
    def __init__(self, movies: list[Movie]):
        self.movies = movies

    def sorted_by_alphabetical(movies: list) -> list:
        """Sort movies by alphabetical."""
        sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
        return sorted_movies

    def add_new_movies(self, movies: Movie):
        """Add a new movies to the program."""
        return self.movies.append(movies)
        # add_new_movies(self.movies)

    def get_all_movies(self, movies: Movie) -> list:
        """Return a list of all films in thriller.

        :return: list of Thriller objects"""
        return self.movies

    def too_old_movies(self, year=None) -> list[list[Any] | Any] | None:

        for i in year <= 1999:
            if movie := self.movies[i]:
                return [movie]
            movie.add_new_movies(year)





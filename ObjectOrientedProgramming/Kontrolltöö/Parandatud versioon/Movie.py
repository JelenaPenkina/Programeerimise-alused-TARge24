import random


class Movie:
    """Represent a general movie."""

    category = "Film"

    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year

    def __repr__(self):
        return f"Movie(name='{self.name}', year={self.year})"

    def get_age(self, current_year=2025):
        return current_year - self.year

    def is_classic(self):
        return self.year < 2000


class Thriller(Movie):
    """Represent a thriller movie. Inherits from Movie."""

    def __init__(self, name: str, year: int, violence_level: int = 5):
        super().__init__(name, year)
        self.violence_level = violence_level

    def __repr__(self):
        return f"Thriller(name='{self.name}', year={self.year}, violence_level={self.violence_level})"

    def is_violent(self):
        return self.violence_level >= 7


if __name__ == "__main__":
    # Test example objects
    m1 = Movie("Inception", 2010)
    t1 = Thriller("Kill Bill", 2003, violence_level=8)

    print(m1)
    print(t1)
    print(m1.get_age())
    print(t1.is_violent())

    # Create 100 movie objects with 60/40 split
    all_movies = []

    # 60 regular movies
    for _ in range(60):
        name = f"Movie{random.randint(1, 100)}"
        year = random.randint(1980, 2024)
        all_movies.append(Movie(name, year))

    # 40 thrillers
    for _ in range(40):
        name = f"Thriller{random.randint(1, 100)}"
        year = random.randint(1980, 2024)
        violence = random.randint(1, 10)
        all_movies.append(Thriller(name, year, violence))

    # Apply a method to all
    for i, movie in enumerate(all_movies, 1):
        print(f"{i}. {movie} — {'Classic' if movie.is_classic() else 'Modern'}")

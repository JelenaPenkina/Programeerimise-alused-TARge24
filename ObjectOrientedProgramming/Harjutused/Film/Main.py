import random
from Film import (Film)
from AnimatedFilm import AnimatedFilm

if __name__ == '__main__':
    films = []
    for _ in range(60):
        films.append(Film(random.choice(["Inception", "Avatar", "Titanic"]), random.randint(90, 180), random.choice(["Action", "Drama", "Sci-Fi"])))

    for _ in range(40):
        films.append(AnimatedFilm(random.choice(["Frozen", "Toy Story", "Moana"]), random.randint(70, 120), "Animation", age_rating=random.choice([3, 6, 12])))

    for film in films:
        print(film)
        if isinstance(film, AnimatedFilm):
            print("Kid friendly:", film.is_kid_friendly())
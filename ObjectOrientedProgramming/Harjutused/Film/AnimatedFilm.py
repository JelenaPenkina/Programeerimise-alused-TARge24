from Film import Film

class AnimatedFilm(Film):
    def __init__(self, title: str, duration: int, genre: str, age_rating: int = 6):
        super().__init__(title, duration, genre)
        self.age_rating = age_rating

    def is_kid_friendly(self):
        return self.age_rating <= 7

    def __repr__(self):
        return f"AnimatedFilm({self.title}, {self.duration}min, {self.genre}, {self.age_rating}+)"


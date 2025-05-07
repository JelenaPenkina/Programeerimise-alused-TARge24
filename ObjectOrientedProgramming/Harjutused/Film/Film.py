class Film:
    """Represents a film."""
    medium = "Digital"

    def __init__(self, title: str, duration: int, genre: str):
        self.title = title
        self.duration = duration  # in minutes
        self.genre = genre

    def is_long(self):
        return self.duration > 120

    def __repr__(self):
        return f"Film({self.title}, {self.duration}min, {self.genre})"
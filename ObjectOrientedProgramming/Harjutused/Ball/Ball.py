class Ball:
    """Represents a ball."""
    material = "Rubber"

    def __init__(self, diameter: int, sport: str):
        self.diameter = diameter
        self.sport = sport

    def bounce(self):
        return f"The {self.sport} ball bounces!"

    def __repr__(self):
        return f"Ball({self.sport}, {self.diameter}cm)"
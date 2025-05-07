from Ball import Ball

class InflatableBall(Ball):
    """A ball that can be inflated."""
    def __init__(self, diameter: int, sport: str, inflated: bool = True):
        super().__init__(diameter, sport)
        self.inflated = inflated

    def deflate(self):
        self.inflated = False

    def inflate(self):
        self.inflated = True

    def __repr__(self):
        return f"InflatableBall({self.sport}, {self.diameter}cm, {'inflated' if self.inflated else 'flat'})"

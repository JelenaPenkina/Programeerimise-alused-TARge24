
class Cup:
    """Represents a cup."""
    material = "Ceramic"  # class variable

    def __init__(self, volume: int, color: str, is_full: bool = False):
        self.volume = volume  # in ml
        self.color = color
        self.is_full = is_full

    def fill(self):
        self.is_full = True

    def empty(self):
        self.is_full = False

    def __repr__(self):
        return f"Cup({self.volume}ml, {self.color}, {'full' if self.is_full else 'empty'})"
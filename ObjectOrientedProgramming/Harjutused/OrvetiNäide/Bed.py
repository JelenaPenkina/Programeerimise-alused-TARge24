"""Class bed"""
import random


class Bed:
    """Class bed"""

    material = 'Puit'

    def __init__(self, width: int, length: int, is_made: bool = False):
        """Initialize a bed object"""
        self.width = width
        self.length = length
        self.is_made = is_made

    def __repr__(self):
        """
        Return representation of the Bed.

        Bed(width, length, is_made, material)
        """
        return f"Bed(width={self.width}, length={self.length}, is_made={self.is_made}, material={self.material})"

    def get_is_made(self) -> str:
        """Return if the bed is madeup."""
        return f'See voodi on korda tehud' if self.is_made else 'See voodi on sassis'

    def get_size(self):
        """Return the size of the bed."""
        return f'Selle voodi suurus on {self.width} x {self.length} cm'

    def fit_people(self):
        """Calculate how many people are accommodated to this bed."""
        return 1 if self.width < 120 else 2

    def accommodates_people(self):
        """Return how many people are accommodated to this bed."""
        return f'Siin saab magada {self.fit_people()} {"inimest" if self.fit_people() > 1 else "inimene"}'
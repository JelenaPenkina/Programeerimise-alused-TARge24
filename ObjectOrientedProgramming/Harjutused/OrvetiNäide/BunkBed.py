"""Class Bunkbed - pärilus"""
import random
import Bed


class BunkBed(Bed):
    """Class BunkBed"""

    def __init__(self, width: int, length: int, is_made: bool = False,
                 floors: int = 2):
        """Initialize a bunk bed object"""
        super().__init__(width, length, is_made)
        self.floors = floors
        self.material = 'Metall'

    def __repr__(self):
        """
      Return representation of the Bed.

      Bed(width, length, is_made, floors, material)
      """
        return f"BunkBed(width={self.width}, length={self.length}, is_made={self.is_made}, floors={self.floors}, material={self.material})"

    def bunk_bed_accommodates_people(self):
        """Calculate how many people are accommodated to this bunk."""
        return f'Siin saab magada {self.floors * self.fit_people()} inimest'
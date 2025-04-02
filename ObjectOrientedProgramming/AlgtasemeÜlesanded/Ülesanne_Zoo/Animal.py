class Animal:
    """Animal class."""

    def __init__(self, name: str, specie: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param specie: animal specie
        """
        self.name = name
        self.specie = specie
        self.age = age

    def __eq__(self, other) -> bool:
        """Check equality based on name and specie."""
        return isinstance(other, Animal) and self.name == other.name and self.specie == other.specie

    def __repr__(self):
        """Represent animal object."""
        return f"Animal('{self.name}', {self.specie}, {self.age})"
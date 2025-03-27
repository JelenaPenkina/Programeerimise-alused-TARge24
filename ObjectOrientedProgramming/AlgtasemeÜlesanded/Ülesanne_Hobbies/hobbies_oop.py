"""Hobbies but OOP."""


class Person:
    """
    Class for people.

    Every person has
    a first name,
    last name and
    list of hobbies.
    """

    def __init__(self, first_name: str, last_name: str, hobbies: list):
        """
        Person constructor.

        :param first_name: first name of the person
        :param last_name: last name of the person
        :param hobbies: list of hobbies
        """
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

    @property  #
    def full_name(self) -> str:
        """
        Get person's full name.

        Combination of first and last name.
        """
        return str(self.first_name) + str(self.last_name)

    @full_name.setter
    def full_name(self, full_name: str):
        names = full_name.split()
        self.first_name = names[0]
        self.last_name = names[-1]

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name

    def has_hobby(self, hobby: str) -> bool:
        """Return true if person has hobby."""
        return hobby in self.hobbies

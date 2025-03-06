"""Simple class"""


class Student:
    """Student class."""

    # CTRL + O aitab avada Methods to Ovverride
    # self tuleb alati klassis esimeseks parameetriks panna
    def __init__(self, name):
        """Initialize a student object."""
        self.name = name
        self.finished = False


if __name__ == '__main__':
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False



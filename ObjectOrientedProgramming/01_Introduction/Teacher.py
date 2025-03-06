"""Teacher class."""


class Teacher:
    """Teacher class."""

    def __init__(self, name="", school=""):
        self.name = name
        self.school = school


if __name__ == "__main__":
    t1 = Teacher()
    t2 = Teacher("Kristjan")
    t3 = Teacher(school="TTHK")

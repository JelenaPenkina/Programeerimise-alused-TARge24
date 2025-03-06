"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Create an empty person."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname="", lastname="", age=""):
        """Initialize student with firstname, lastname and age."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    Empty()
    # 3 x person usage
    p1 = "Lena", "P", "28"
    print(p1)
    p2 = "Mark", "Kuusik", "30"
    print(p2)
    p3 = "Robert", "Tarlap", "23"
    print(p3)
    # 3 x student usage
    s1 = Student('Mark', 'Kuusik', '30')
    s2 = Student('Tauno', 'Tippi', '35')
    s3 = Student("Lena", "P", "28")

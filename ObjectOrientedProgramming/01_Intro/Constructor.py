"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Person with firstname, lastname and age."""
        self.firstname = ''
        self.lastname = ''
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Construct student with firstname, lastname and age."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    e = Empty()

    p1 = Person()
    p1.firstname = 'John'
    p1.lastname = 'Doe'
    p1.age = 20
    p2 = Person()
    p2.firstname = 'Jane'
    p2.lastname = 'Woman'
    p2.age = 30
    p3 = Person()
    p3.firstname = 'Spider'
    p3.lastname = 'Smith'
    p3.age = 40

    s1 = Student(firstname='John', lastname='Doe', age=25)
    s2 = Student(firstname='Jane', lastname='Woman', age=19)
    s3 = Student(firstname='Spider', lastname='Man', age=45)
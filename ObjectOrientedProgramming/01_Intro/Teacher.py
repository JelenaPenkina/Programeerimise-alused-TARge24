"""Teacher"""


class Teacher:
    """Teacher class."""

    def __init__(self):
        super().__init__()

    def __init__(self, name='', school=''):
        self.name = name
        self.school = school


if __name__ == '__main__':
    t1 = Teacher()
    t2 = Teacher('Juhan')
    t3 = Teacher(school='TTHK')

    print(t1.name)
    print(t2.name)
    print(t3.school)
"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id, status='Active'):
        """Initialize for student."""
        self.__id = id
        self.__name = name
        self.__status = status

    def get_id(self):
        """
        Get id of student.

        :param self:
        :return: Student id
        """
        return self.__id

    def set_name(self, name):
        """
        Set new name.

        :param self:
        :param name: New name
        """
        self.__name = name

    def get_name(self):
        """Get student name."""
        return self.__name

    def set_status(self, status):
        """Set student status."""
        allowed = ["Active", "Expelled", "Finished", "Inactive"]

        if status in allowed:
            self.__status = status

    def get_status(self):
        """
        Get student status.

        :param self:
        :return:
        """
        return self.__status

    def __str__(self):
        """To string."""
        return f'{self.__id} {self.__name} {self.__status}'


if __name__ == '__main__':
    s1 = Student(1, 'Jhon')
    s1.set_status('')
    print(s1)

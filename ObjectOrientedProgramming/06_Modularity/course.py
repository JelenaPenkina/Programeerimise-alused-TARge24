"""
See klass hoiab infot ühe õppeaine kohta.

Loo järgmised meetodid:

def __init__(self, name: str) - konstruktor, kuhu saab kaasa anda kursuse nime.
Arvatavasti on vaja siin konstruktoris luua info ka selle jaoks, et hoida
õpilaste hindeid.

def get_grades(self) -> list[tuple[Student, int]] - meetod tagastab järjendi
õpilaste tulemustest. Järjendi iga element on ennik (tuple), kus esimene
element on õpilase objekt ja teine on tema hinne.
Hindeid pannakse School klassis oleva meetodiga add_student_grade().
Mõistlik on kursuse klassi lisada mingi abistav meetod, millega hinnet lisada.

def get_average_grade(self) -> float - tagastab kursuse keskmise hinde.
Ehk siis keskmine kõikidest sellele kursusel antud hinnetest. Kui hindeid pole,
siis tagastab meetod -1.

def __repr__(self) - tagastab "ilusa" sõne kuju antud objektist, ehk tagastab
kursuse nime. Kuigi __str__ meetodi realiseerimine annaks suuresti sama tulemuse,
siis __repr__ eelis on see, et ka listi ja enniku jm andmestruktuuri sees
näidatakse objekti vastavalt määratud sõne kujul.

"""
# import student
from typing import Any


class Course:
    #
    # def __init__(self, name: str, course) -> None:
    #     self.__student = None
    #     self.__name = name
    #     self.__course = course
    #
    # def get_grades(self) -> list[tuple[Student, int]]:
    #     pass
    #
    # def get_average_grade(self) -> float:
    #     return sum(self.__student) / len(self.__course)
    #
    # def __repr__(self):
    #     return self.__course.__name
    #

    # õpetaja näidis

    def __init__(self, name: str):
        """
        Initialize Course object.

        grades contains a list of tuples (student, grade).
        :param name: name of the course.
        """
        super().__init__()
        self.name = name
        self.grades = []

    def get_grades(self) -> list[tuple[Any, float]]:
        """
        Return grades of course.

        :return: list of tuples (student, grade).
        """
        return self.grades

    def get_average_grade(self) -> float:
        """
        Get average grade of course.

        :return: Total average grade of course.
        """
        if len(self.grades) == 0:
            return -1
        total = 0
        for grade in self.grades:
            total += grade[1]
        return total / len(self.grades)

    def add_grade(self, student_grade: tuple[Any, float]):
        """
        Add grade of course.

        :param student_grade: tuple of student grade.
        """
        self.grades.append(student_grade)

    def __repr__(self):
        """
        Represent course.

        :return: course name.
        """
        return self.name

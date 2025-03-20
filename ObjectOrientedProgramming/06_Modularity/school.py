"""
Kool koondab kokku õpilased ja kursused.

Loo järgmised meetodid:

def __init__(self, name) - konstruktor, kuhu saab kaasa anda kooli nime.
Kooli nimi tuleb salvestada muutujasse self.name. Lisaks on mõistlik luua
üks muutuja õpilaste ja üks muutuja kursuste hoidmiseks.

def add_course(self, course: Course) - kursus lisatakse kooli. Kui selline
kursus on juba olemas, siis seda teistkordselt ei lisata.

def add_student(self, student: Student) - õpilane lisatakse kooli. Kui selline
õpilane on juba olemas, siis teda teistkordselt ei lisata. Ühtlasi kui õpilane
lisatakse kooli, siis määratakse talle unikaalne id (set_id() meetod õpilasel).

def add_student_grade(self, student: Student, course: Course, grade: int) - lisatakse
hinne õpilasele konkreetse kursuse eest. Hinne lisatakse ainult siis, kui õpilane on
selles koolis ja kursus on selles koolis olemas. Hinne peaks minema ka õpilase ja
kursuse külge (selleks, et nende kaudu saada hindeinfot kätte). Seega siin on mõistlik
välja kutsuda vastavalt õpilasel ja kursusel mingeid oma loodud meetodeid, mis
salvestavad hinded nende objektide külge. Siin ei pea arvestama olukorraga, kui
lisatakse hinne kursusele, kus juba on hinne (sellist olukorda ei testita).
Kui on soovi, võid proovida sellises olukorras uut hinnet ignoreerida või kirjutad vana üle.
Hinde väärtust kontrollima ei pea. See on täisarv vahemikus 1-5 (kaasa arvatud).

get_students(self) -> list[Student] - tagastab õpilaste järjendi. Elemendid on Student
objektid ning elemendid on järjendis nende lisamise järjekorras.

get_courses(self) -> list[Course] - tagastab kursuste järjendi. Elemendid on Course
objektid ning elemendid on järjestatud nende lisamise järjekorras.

def get_students_ordered_by_average_grade(self) -> list[Student] - tagastab õpilaste järjendi järjestatuna keskmise hinde järgi nii, et eespool on õpilane, kelle keskmine hinne on kõrgem. Siin ei pea midagi erilist tegema õpilastega, kelle keskmine hinne on sama (need võivad jääda samasse järjekorda).


"""
from course import Course
from student import Student


class School:
    # def __init__(self, name: str):
    #     self.__grade = None
    #     self.__student = None
    #     self.__course = None
    #     self.__name = name
    #
    # def add_course(self, course: Course):
    #     self.__course = course
    #
    # def add_student(self, student: Student):
    #     self.__student = student
    #
    # def add_student_grade(self, student: Student, course: Course, grade: int):
    #     self.__student = student
    #     self.__course = course
    #     self.__grade = grade

    # õpetaja näidis

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.courses = []
        self.students = []
        self.next_student_id = 1

    def add_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)
            student.set_id(self.next_student_id)
            self.next_student_id += 1

    def add_student_grade(self, student: Student, course: Course, grade: int):
        if course not in self.courses or student not in self.students:
            return
        course.add_grade((student, grade))
        student.add_grade((course, grade))

    def get_students(self) -> list[Student]:
        return self.students

    def get_courses(self) -> list[Course]:
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        return self.students
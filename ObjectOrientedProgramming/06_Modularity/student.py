"""
Klass hoiab ühe õpilase infot.

Loo järgmised meetodid:

def __init__(self, name: str) - konstruktor, kuhu saab kaasa anda õpilase nime.
Siin on vaja luua muutuja(d) õpilase hinnete hoidmiseks. Lisaks tuleb luua muutuja
õpilase id jaoks, mille väärtust alguses peab olema None.

def set_id(self, id: int) - õpilasele määratakse unikaalne identifikaator.
Kui identifikaator on juba määratud, siis teist korda seda üle kirjutada ei
saa (sellisel juhul lihtsalt ignoreeritakse uue väärtuse lisamist)

def get_id(self) -> int - tagastab õpilase identifikaatori

def get_grades(self) -> list[tuple[Course, int]] - tagastab järjendi õpilase tulemustest.
Iga element on ennik (tuple), mille esimene element on kursuse objekt ja teine element
on hinne sellel kursusel. Hindeid pannakse School klassis oleva meetodiga
add_student_grade(). Mõistlik on õpilase klassi lisada mingi abistav meetod,
millega hinnet lisada.

def get_average_grade(self) - tagastab õpilase keskmise hinde. Kui õpilasel hindeid pole,
 agastab meetod -1.

def __repr__(self) -> str - tagastab objekti sõnekuju. Siin klassis tagastab õpilase nime.
"""
from course import Course

class Student:

    # def __init__(self, name:str, id:None):
    #     self.name = name
    #     self.id = id
    #
    # def set_id(self, id:int):
    #     self.id = id
    #
    # def get_id(self) -> int:
    #     return self.id
    #


    # õpetaja näidis

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.grades = []
        self.id = None

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        return self.id

    def get_grades(self) -> list[tuple[Course, int]]:
        return self.grades

    def get_average_grade(self):
        if len(self.grades) == 0:
            return -1
        total = 0
        for grade in self.grades:
            total += grade[1]
        return total / len(self.grades)

    def add_grade(self, student_grade: tuple[Course, float]):
        """
        Add grade of Student.

        :param student_grade: tuple of student grade.
        """
        self.grades.append(student_grade)

    def __repr__(self) -> str:
        pass

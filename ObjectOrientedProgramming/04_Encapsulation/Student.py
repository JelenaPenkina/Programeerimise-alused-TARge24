"""
Tuleb luua klass Student ning kasutada "privaatseid" muutujaid. Objekti loomisel
(konstruktoris) võetakse vastu kaks väärtust selles järjekorras: nimi (sõne) ja id (täisarv).
Seega peab konstruktor aktsepteerima kahte parameetrit. Need väärtused salvestatakse "privaatsetesse"
muutujatesse. Lisaks on igal tudengil eraldi info staatuse kohta. Vaikimisi staatus
(kui tudeng luuakse) on "Active".

Tudengi objektil on võimalik muuta nime ja staatust. Id väärtust jooksvalt enam muuta ei saa.
Staatuse muutmisel on kindlad reeglid.

Tudengi objektil peavad olema järgmised meetodid:

get_id(self) - tagastab algselt tudengile määratud id.
set_name(self, name) - määrab tudengile uue nime
get_name(self) - tagastab tudengi hetke nime
set_status(self, status) - määrab tudengile uue staatuse, aga seda vaid juhul, kui
staatuse väärtus on üks järgmistest: Active, Expelled, Finished, Inactive. Muul juhul staatust ei
muudeta (viga ka ei anta - funktsioon lihtsalt ei tee midagi)
get_status(self) - tagastab tudengi hetke staatuse
"""


class Student:
    """Represent student with name, id and status."""
    STATUS_ACTIVE = "Active"
    STATUS_EXPELLED = "Expelled"
    STATUS_FINISHED = "Finished"
    STATUS_INACTIVE = "Inactive"
    statuses = [STATUS_ACTIVE, STATUS_EXPELLED, STATUS_FINISHED,
                STATUS_INACTIVE]

    def __init__(self, name: str, student_id: int):
        self.__name = name
        self.__id = student_id
        self.__status = Student.STATUS_ACTIVE

    def get_id(self):
        """

        :return:
        """
        return self.__id

    def set_name(self, name: str):
        """

        :param name:
        """
        self.__name = name

    def get_name(self):
        """

        :return:
        """
        return self.__name

    def set_status(self, status: str):
        """

        :param status:
        """
        if status in Student.statuses:
            self.__status = status

    def get_status(self):
        """

        :return:
        """
        return self.__status
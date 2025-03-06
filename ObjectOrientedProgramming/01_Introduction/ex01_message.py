"""
Ülesanne 1: Sõnum
Kirjuta kood, mis hoiab sõnumi andmeid objektis.
Igal sõnumil on sisu (sõne), autor (sõne), aeg () ja meeldimiste arv (täisarv).

Klassis peaks olema meetod, mis arvutab populaarsuse:
meeldimiste arv sõnumi loomisest möödunud ajaühiku kohta(likes / time).

Edasiarendus:Kasuta aja asemel päriselt kuupäeva/kellaaja objekti.
"""
import datetime


class Message:

    def __init__(self, content="", autor="", time=datetime.datetime.now(), likes=0):
        """Initialize message with parameters."""
        self.content = content
        self.autor = autor
        self.time = time
        self.likes = likes

    def get_popularity(self, time_unit):
        """
        Calculate message popularity.

        :returns likes/time in time_units
        """
        duration = datetime.datetime.now()- self.posted
        time_in_unit = duration.total_seconds()
        return self.likes / time_in_unit

if __name__ == '__main__':
    m1 = Message(likes=50)
    print(m1.get_popularity(60))


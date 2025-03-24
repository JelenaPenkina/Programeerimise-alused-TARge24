"""
Ülesanne1: Sõnum
Kirjuta kood, mis hoiab sõnumi andmeid objektis.
Igal sõnumil on sisu(sõne), autor(sõne), aeg() ja meeldismite arv(täisarv)

Klassis peaks olema meetod,
mis arvutab populaarsuse: meeldimiste arv sõnumi loomisest möönud ajaühiku kohta
(likes/times)

Edasiarendus:
Kasuta ja asemel pärislt kuupäeva/kellaaja objekti.
"""

import datetime


class Message:
    """
    Class Message.
    """

    def __init__(self, message='', author='', posted=datetime.datetime.now(),
                 likes=0):
        """Make constructor"""
        self.message = message
        self.author = author
        self.posted = posted
        self.like_count = likes

    def get_popularity(self, time_unit_seconds):
        """Calculate popularity."""
        duration = datetime.datetime.now() - self.posted
        time_in_units = duration.total_seconds() / time_unit_seconds
        return self.like_count / time_in_units


if __name__ == '__main__':
    m1 = Message("Hello World!", "mina", likes=555)

    print(m1.get_popularity(60))
    print(m1.posted)
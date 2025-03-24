"""
Lisa kõikidesse sõnastikesse järgmised sõnad:

headaega - goodbye - arrivederci
pott - pot - pentola
sõnastik - dictionary - dizionario
Tõlgi (väljastage ekraanile) järgmised sõnad:

üks -> itaalia
ciao - > eesti
dog -> itaalia
pentola - inglise
"""
from Python_koolis_5_3 import dictonary
from Python_koolis_5_3 import e_inglise, e_itaalia


def add_new_word(est, eng, ita):
    dictonary.dic.english[est] = eng
    dictonary.dic.italian[est] = ita
    e_inglise[eng] = est
    e_itaalia[ita] = est


add_new_word('headaega', 'goodbye', 'arrivederci')
add_new_word('pott', 'pot', 'pentola')
add_new_word('sõnastik', 'dictionary', 'dizionario')

if __name__ == '__main__':
    print(dictonary.dic.english)
    print(dictonary.dic.italian)
    print(e_itaalia)
    print(e_inglise)
    print(dictonary.dic.italian['üks'])
    print(e_itaalia['ciao'])
    print(dictonary.dic.italian[e_inglise['dog']])
    print(dictonary.dic.english[e_itaalia['pentola']])
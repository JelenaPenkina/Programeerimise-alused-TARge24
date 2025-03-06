"""
Tõlgi (väljasta ekraanile) järgmised sõnad:

    tere -> inglise k, itaalia k
    auto -> itaalia k
    kass - > inglise k
    üks -> itaalia k
    kolm -> inglise k
"""
import python_koolis_5_1_dictionary as dictionary

ONE_KEY = 'üks'
THREE_KEY = 'kolm'

if ONE_KEY not in dictionary.italian:
    dictionary.italian[ONE_KEY] = "uno"
if THREE_KEY not in dictionary.english:
    dictionary.english[THREE_KEY] = "three"

if __name__ == '__main__':
    print(f"tere -> inglise k ='{dictionary.english['tere']}', itaalia k ='{dictionary.italian['tere']}'")
    print(f"üks - itaalia k = '{dictionary.italian[ONE_KEY]}'")
    print(f"kolm - inglise k = '{dictionary.english[THREE_KEY]}'")

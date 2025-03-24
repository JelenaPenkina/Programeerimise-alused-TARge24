"""
Tõlgi (väljasta ekraanile) järgmised sõnad:

tere -> inglise k, itaalia k
auto -> itaalia k
kass - > inglise k
üks -> itaalia k
kolm -> inglise k
"""
import Python_koolis_5_1 as dic

ONE_KEY = 'üks'
THREE_KEY = 'kolm'

if ONE_KEY not in dic.italian:
    dic.italian[ONE_KEY] = 'uno'
if THREE_KEY not in dic.english:
    dic.english[THREE_KEY] = 'three'
if __name__ == '__main__':
    print(dic.english['tere'], dic.italian['tere'])
    print(dic.italian['auto'])
    print(dic.english['kass'])
    print(dic.italian[ONE_KEY])
    print(dic.english[THREE_KEY])
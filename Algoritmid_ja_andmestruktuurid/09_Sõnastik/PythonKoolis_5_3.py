"""
Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole
mitte eesti keeles, vaid vastavalt kas inglise või itaalia keeles.
Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad.
"""

import Python_koolis_5_2 as dictonary


def reverse_dictionary(dictionary):
    reversed_dictionary = {}
    for k, v in dictionary.items():
        reversed_dictionary[v] = k
    return reversed_dictionary


e_inglise = reverse_dictionary(dictonary.dic.english)

e_itaalia = reverse_dictionary(dictonary.dic.italian)
# for k, v in dictonary.dic.italian.items():
#    e_itaalia[v]= k
if __name__ == '__main__':
    print(e_itaalia)
    print(e_inglise)
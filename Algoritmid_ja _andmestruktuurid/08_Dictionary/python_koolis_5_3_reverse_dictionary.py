"""
    Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole mitte eesti keeles,
    vaid vastavalt kas inglise või itaalia keeles.
    Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad
"""
import Python_koolis_5_2_translate as second

def reverse_dictionary(dictionary):
    reversed_dictionary = {}
    for key, value in dictionary.items():
        reversed_dictionary[value] = key
    return reversed_dictionary

e_english = reverse_dictionary(second.dictionary.english)
e_italian = reverse_dictionary(second.dictionary.italian)

if __name__ == '__main__':
    print(e_english)
    print(e_italian)

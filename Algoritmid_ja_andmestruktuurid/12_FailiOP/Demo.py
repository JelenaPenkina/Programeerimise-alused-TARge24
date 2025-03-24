"""Faili operatsioonide demo"""

file_name = "test.txt"

with open(file_name, 'a', encoding='utf-8') as f:
    f.write('tere veelkord\n')

with open(file_name, 'r', encoding='utf-8') as f:
    print(f.readlines())
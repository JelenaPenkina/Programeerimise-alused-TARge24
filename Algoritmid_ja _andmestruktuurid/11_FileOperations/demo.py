""" Faili operatsioonide demo """

file_name = "test.txt"

with open(file_name, "a", encoding="utf-8") as file:
    file.write("hello world\n")

with open(file_name, encoding="utf-8") as file:
    print(file.readlines())
    file.write("error")

# print("Hello World)  # Jutumärgid lõpetamata


# print("Hello World") # Taande viga


# if __name__ == '__main__':
#    print("Hello World")      # Puuduv taane viga

# print(undeclared_variable + 10)  # --> NameError


variable = "viis"


# print(variable + 10)  # can only concatenate str (not "int") to str
# print(10 + variable)    # unsupported operand type(s) for +: 'int' and 'str'

def third(a):
    print(int(a))  # Attempt to convert string <The output is called 'Stack Trace'> to int and print it out


def second(a, b):
    c = a + b
    print(c)  # --> The output is called 'Stack Trace'

    # Calling the third function
    third(c)


def first():
    # Calling the second function
    second("The output is called ", "'Stack Trace'")


first()

# print("Hello" World) #Jutumärgid lõpetamata

# print("Hello World")  # Taande viga

# if __name__ == '__main__':
# print("Hello World")  #Puutuv taande


# print(undeclared_variable + 10) #is not defined

variable = 'viis'


# print(variable + 10) # --> TypeError: must be str, not int (cannot concatenate objects)

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
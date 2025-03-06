class Dog:

    # Class variable
    name = "Some name"

    # Class constructor
    def __init__(self, new_name):
        # Assign class variable to new value
        Dog.name = new_name

    def bark(self):
        print(Dog.name + " says: Woof!")

    def roll(self):
        print("*rolling*")

    def greet(self):
        print(Dog.name + " greets you!")

    def speak(self):
        print("I cannot")

    # Returns the current dog's name
    def get_name(self):
        return Dog.name

# We do not need to create an object to access the class variable
print(Dog.name)  # --> Some name

dog1 = Dog("Clyde")
dog1.bark()  # --> Clyde says: Woof!
dog1.greet()  # --> Clyde greets you!
print(dog1.get_name())  # --> Clyde
print(Dog.name)  # --> Clyde

dog2 = Dog("Jenkins")
dog2.bark() # --> Jenkins says: Woof!
dog2.greet() # --> Jenkins greets you!
print(dog2.get_name())  # --> Jenkins
print(Dog.name)  # --> Jenkins

print(dog1.get_name())  # Jenkins #Dog.Name was changed in dog2 constructor
dog1 = Dog("Clyde")
dog1.bark() 
print(Dog.get_name())
# Assign new value to the variable name
Dog.name = "Some random dog name"
print(Dog.name)  # --> Some random dog name
class Dog:
    # Class variable
    names = []
    sequence = 1

    # Class constructor
    def __init__(self, new_name):
        # Assign class variable to new value
        self.name = new_name
        self.id_number = Dog.sequence
        Dog.sequence += 1
        Dog.names.append(new_name)

    def bark(self):
        print(f"Dog #{self.id_number} {self.name} +  says: Woof!")

    def roll(self):
        print("*rolling*")

    def greet(self):
        """
        greet.
        """
        print(self.name + " greets you!")

    def speak(self):
        """
        Speak.
        """
        print("I cannot")

    def get_name(self):
        """
        Returns the current dog's name.
        :return:
        """
        return self.name

    @classmethod
    def get_all_names(cls):
        """
        Get all dog names.
        :return:
        """
        return cls.names


# We do not need to create an object to access the class variable
# print(Dog.name)  # --> Some name

dog1 = Dog("Clyde")
dog1.bark()  # --> Clyde says: Woof!
dog1.greet()  # --> Clyde greets you!
print(dog1.get_name())  # --> Clyde
# print(Dog.name)  # --> Clyde

dog2 = Dog("Jenkins")
dog2.bark()  # --> Jenkins says: Woof!
dog2.greet()  # --> Jenkins greets you!
print(dog2.get_name())  # --> Jenkins
# print(Dog.name)  # --> Jenkins

dog1.bark()
print(Dog.get_all_names())

# Assign new value to the variable name
Dog.name = "Some random dog name"
# print(Dog.name)  # --> Some random dog name
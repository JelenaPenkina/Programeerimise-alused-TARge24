from operator import length_hint

user_age = int(input("Enter your age: "))
user_name = input("Enter your name: ")

for i in range(user_age - 1):
    print(f"Tere {user_name}!")
print(user_name[len(user_name) - 3:])
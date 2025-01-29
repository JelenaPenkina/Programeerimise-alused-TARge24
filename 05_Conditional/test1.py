# Write your code here

first_name = "James"
last_name = "Bond"

full_name = first_name + ' ' + last_name


def self_description_sentence():
    print(f"My name is {last_name}, {first_name} {last_name}.")


cake = "vahukoormarjadtäidispõhi"
print(cake[0:8] + "\n" + cake[8:14] + "\n" + cake[14:20] + "\n" + cake[20:])

original_string = "Programming is fun!"
backwards = original_string[::-1]

every_other = original_string[::2]
print(every_other)

first_word_reversed = original_string.split()
print(first_word_reversed)

if __name__ == '__main__':
    self_description_sentence()

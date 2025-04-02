from hobbies_oop import Person


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    return list(filter(lambda person: person.has_hobby(hobby), people_list))


def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """

    # Sorteerin inimesed nime järgi
    sorted_people = sorted(people_list, key=lambda person: person.full_name)

    # Loo uus nimekiri uute objektidega, kus hobid on sorteeritud
    return [Person(person.first_name, person.last_name, sorted(person.hobbies)) for person in sorted_people]
    # return sorted(people_list, key=lambda person: (-len(person.hobbies), person.full_name))
    # miinus(-) märk paneb hobbide koguse nullist alates


def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    return sorted(people_list, key=lambda person: (len(person.hobbies), person.full_name))

    # least_amount = 0
    # for person in people_list:
    #     least_amount = min(least_amount, person.amount)


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return the list of people but sorted alphabetically by their full name.

    Also sort their list of hobbies.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_people = sorted(people_list, key=lambda person: person.hobbies)
    for person in sorted_people:
        person.hobbies = sorted(person.hobbies)
    return sorted_people


if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    people = [person1, person2, person3]
    person1.full_name = "Teet Kukk"
    print(person1.first_name)
    print(person1.full_name)
    print(sort_by_most_hobbies(people))  # -> [Jeff Bezos, Elon Musk, Mari Kukk]
    print("[Jeff Bezos", "Elon Musk", "Mari Kukk]\n")
    print(sort_by_least_hobbies(people))  # -> [Elon Musk, Mari Kukk, Jeff Bezos]
    print(filter_by_hobby(people, "space"))  # -> [Elon Musk, Jeff Bezos]
    print(sort_people_and_hobbies(people))  # -> [Elon Musk, Jeff Bezos, Mari Kukk]
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']

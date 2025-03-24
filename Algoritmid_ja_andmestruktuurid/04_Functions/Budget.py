room_rent = 55
food_budget_per_person = 10


def full_budget(guest_number: int) -> str:
    """returns party budget"""
    return f'Maksimaalne eelarve on {guest_number * food_budget_per_person + room_rent} eurot'


def min_max_budget():
    """prints min and max budget"""
    invited_quest = int(input("Please enter your invited quest: "))
    coming_quest = int(input("Please enter your coming quest: "))
    print(full_budget(invited_quest))
    return f'Minimaalne eelarve on {coming_quest * food_budget_per_person + room_rent} eurot'


if __name__ == '__main__':
    print(min_max_budget())
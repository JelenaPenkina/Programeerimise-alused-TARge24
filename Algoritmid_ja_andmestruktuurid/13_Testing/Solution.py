"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 5 <= time <= 17:
        return coffee_needed
    elif 18 <= time <= 24:
        return True
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if (a == b == c) and a == 5:
        return 10
    elif a == b == c:
        return 5
    elif not a == b and not a == c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int,
                ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    max_big_used = min(ordered_amount // 5, big_baskets)

    remaining_weight = ordered_amount - (max_big_used * 5)

    if remaining_weight <= small_baskets:
        return remaining_weight
    else:
        return -1


if __name__ == '__main__':
    print(students_study(5, False))
    # print(fruit_order(1, 1001, 5009))
    # print(lottery(0, 0, 0))

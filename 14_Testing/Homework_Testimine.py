"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    pass


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    pass


def fruit_order(small_baskets: int, big_baskets: int,
                ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    pass


import solution


def test_student_study__day():
    assert solution.student_study(5, False) is False
    assert solution.student_study(17, False) is False


def test_lottery__jackpot():
    """All numbers are winners"""
    assert lottery(5, 5, 5) == 10


def test_lottery__all_same__not_winners__medium():
    """All numbers are same but not winners."""
    assert solution.lottery(1, 1, 1) == 5
    assert solution.lottery(0, 0, 0) == 5


def test_lottery_small_prize():
    """b and c differ from a"""
    assert solution.lottery(1, 2, 3) == 1
    assert solution.lottery(1, -2, 3) == 1


def test_lottery_no_prize():
    """a equals b or c"""
    assert solution.lottery(1, 1, 2) == 0
    assert solution.lottery(2, 1, 2) == 0
    assert solution.lottery(0, 0, 2) == 0


def test_fruit_order__exact_amount_small_baskets():
    """All small baskets are use """
    assert solution.fruit_order(1, 0, 1) == 1
    assert solution.fruit_order(10, 0, 10) == 10
    assert solution.fruit_order(1000, 0, 1000) == 1000


def test_fruit_order__missing_small_baskets():
    """Not enough small baskets are supplied"""
    assert solution.fruit_order(1, 0, 2) == -1
    assert solution.fruit_order(10, 0, 11) == -1
    assert solution.fruit_order(1000, 0, 1001) == -1


def test_fruit_order__big_used_first():
    """Big baskets must be filled first"""
    assert solution.fruit_order(5, 1, 5) == 0
    assert solution.fruit_order(15, 3, 15) == 0
    assert solution.fruit_order(5, 1, 10) == 5


def test_fruit_order__zeros():
    """Zero baskets, Zero orders"""
    assert solution.fruit_order(0, 0, 0) == 0
    assert solution.fruit_order(0, 0, ) == -1


def test_fruit_order__missing_big_baskets():
    """Not enough (big) baskets"""
    assert solution.fruit_order(4, 2, 15) == -1
    assert solution.fruit_order(0, 2, 15) == -1
    assert solution.fruit_order(4, 199, 1000) == -1


def test_fuit_order__only_big_exact_match():
    """Exactly enough only big baskets."""
    assert solution.fruit_order(0, 2, 10) == 0
    assert solution.fruit_order(0, 20, 100) == 0
    assert solution.fruit_order(0, 1, 5) == 0
    assert solution.fruit_order(0, 100, 500) == 0


def test_fuit_order__only_big_excess_no_match():
    """Exactly enough only big baskets."""
    assert solution.fruit_order(0, 20, 11) == -1
    assert solution.fruit_order(0, 22, 104) == -1
    assert solution.fruit_order(0, 2, 6) == -1
    assert solution.fruit_order(0, 1000, 502) == -1


def test_fruit_order__only_small_more_than_required():
    """Only small more than needed."""
    assert solution.fruit_order(20, 0, 10) == 10
    assert solution.fruit_order(220, 0, 100) == 100
    assert solution.fruit_order(9, 0, 5) == 5
    assert solution.fruit_order(1000, 0, 500) == 500


def test_fuit_order__match_with_more_than_5_smalls():
    """Use all smalls some bags"""
    assert solution.fruit_order(11, 3, 23) == 8


def test_fuit_order__use_all_small_some_bigs():
    """Surplus of all"""
    assert solution.fruit_order(3, 5, 23) == 3


def test_fuit_order__enough_bigs_not_enough_smalls():
    """Missing small"""
    assert solution.fruit_order(2, 9, 33) == -1


def test_fuit_order__not_enough_with_more_than_5_smalls():
    """Not enough"""
    assert solution.fruit_order(12, 4, 33) == -1


def test_fuit_order__enough_bigs_not_enough_smalls_large_number():
    """Not enough large numbers"""
    assert solution.fruit_order(3, 10000, 39404) == -1

def test_fuit_order__match_large_numbers():
    """Match large numbers"""
    assert solution.fruit_order(10003,10000,60003) == 10003

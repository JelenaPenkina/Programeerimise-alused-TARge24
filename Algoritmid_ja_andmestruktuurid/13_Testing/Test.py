"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False


def test__students_study__student_study__night_coffee_false():
    """During night with coffee students do not study."""
    assert students_study(3, False) is False


def test__student_study__day_coffee_true():
    """During day with coffee students study is True."""
    assert students_study(12, True) is True


def test__student_study__day_coffee_false():
    """During day with coffee students study is False."""
    assert students_study(12, False) is False


def test__student_study__evening_coffee_false():
    """During evening coffee study is False."""
    assert students_study(19, False) is True


def test__student_study__evening_coffee_true():
    """During evening coffee study is True."""
    assert students_study(19, True) is True


def test__student_study__evening_edge_case_coffee_true():
    """During evening edge coffee study is True."""
    assert students_study(18, True) is True
    assert students_study(24, True) is True


def test__student_study__evening_edge_case_coffee_false():
    """During evening edge coffee study is False."""
    assert students_study(24, False) is True
    assert students_study(18, False) is True


def test__student_study__night_edge_case_coffee_true():
    """During night edge coffee study is True."""
    assert students_study(1, True) is False
    assert students_study(4, True) is False


def test__student_study__night_edge_case_coffee_false():
    """During night edge coffee study is False."""
    assert students_study(1, False) is False
    assert students_study(4, False) is False


def test__student_study__day_edge_case_coffee_true():
    """During day edge coffee study is True."""
    assert students_study(5, True) is True
    assert students_study(17, True) is True


def test__student_study__day_edge_case_coffee_false():
    """During day edge coffee study is False."""
    assert students_study(5, False) is False
    assert students_study(17, False) is False


def test__lottery__all_fives():
    """Lottery all fives."""
    assert lottery(5, 5, 5) == 10


def test__lottery__all_same_positive():
    """Lottery all same postitive."""
    assert lottery(3, 3, 3) == 5


def test__lottery__all_same_negative():
    """Lottery all same negative."""
    assert lottery(-3, -3, -3) == 5


def test__lottery__all_same_zero():
    """Lottery all same zero."""
    assert lottery(0, 0, 0) == 5


def test__lottery__a_b_same_c_diff():
    """Lottery all same C diff."""
    assert lottery(3, 3, 2) == 0


def test__lottery__a_c_same_b_diff():
    """Lottery all same B diff."""
    assert lottery(3, 2, 3) == 0


def test__lottery__b_c_same_a_diff():
    """Lottery all same A diff."""
    assert lottery(3, 2, 2) == 1


def test__lottery__all_diff():
    """Lottery all diff."""
    assert lottery(1, 2, 3) == 1


def test__fruit_order__all_zero():
    """Fruit order all zero."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_small():
    """Fruit order zero amount zero small."""
    assert fruit_order(0, 1, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """Fruit order zero amount zero big."""
    assert fruit_order(4, 0, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """Fruit order zero amount zero others not zero."""
    assert fruit_order(1, 2, 0) == 0


def test__fruit_order__only_big_exact_match():
    """Fruit order only big exact match."""
    assert fruit_order(0, 3, 15) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """Fruit order only big not enough."""
    assert fruit_order(0, 2, 15) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Fruit order only big more than required match."""
    assert fruit_order(0, 4, 15) == 0


def test_fruit_order__only_big_more_than_required_no_match():
    """Fruit order only big more than required no match."""
    assert fruit_order(0, 4, 18) == -1


def test__fruit_order__only_small_match_more_than_5_smalls():
    """Fruit order only small match more than 5 smalls."""
    assert fruit_order(6, 0, 6) == 6


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """Fruit order only small not enough more than 5 smalls."""
    assert fruit_order(6, 0, 7) == -1


def test__fruit_order__only_small_more_than_required():
    """Fruit order only small more than required match."""
    assert fruit_order(7, 0, 6) == 6


def test__fruit_order__match_with_more_than_5_smalls():
    """Fruit order match with more than 5 smalls."""
    assert fruit_order(13, 1, 13) == 8


def test__fruit_order__all_positive_exact_match():
    """Fruit order all positive exact match."""
    assert fruit_order(5, 2, 15) == 5


def test__fruit_order__use_all_smalls_some_bigs():
    """Fruit order use all smalls some bigs."""
    assert fruit_order(3, 3, 13) == 3


def test__fruit_order__use_some_smalls_some_bigs():
    """Fruit order use some smalls some bigs."""
    assert fruit_order(3, 3, 12) == 2


def test__fruit_order__not_enough():
    """Fruit order not enough."""
    assert fruit_order(5, 5, 55) == -1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Fruit order enough big not enough smalls."""
    assert fruit_order(1, 6, 27) == -1


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """Fruit order not enough with more than 5 smalls."""
    assert fruit_order(6, 2, 17) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Fruit order enough big not enough smalls large number."""
    assert fruit_order(1, 200, 102) == -1


def test__fruit_order__match_large_numbers():
    """Fruit order match large numbers."""
    assert fruit_order(505, 101, 1001) == 496

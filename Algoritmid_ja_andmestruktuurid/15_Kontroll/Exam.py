"""Show highest grade."""


def show_highest_grade(grade1: int, grade2: int) -> None:
    """
    Print "Highest grade: GRADE" where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"
    1, 2 => "Highest grade: 1"
    """
    print(f'Highest grade: {grade1 if grade1 > grade2 else grade2}')


"""Camel case word counter."""


def camel_case_word_counter(input_string: str) -> int:
    """
    Count words.

    Given input_string of concatenation of one or more words consisting of English letters
    where first word is lowercase and other words start with uppercase, count and return number
    of words. In case of empty string, return zero.

    camel_case_word_count("hello") => 1
    camel_case_word_count("") => 0
    camel_case_word_count("someMoreWordsHere") => 4

    :param input_string: camel cased string.
    :return: integer which shows number of words in camel cased string.
    """
    counter = 1
    if input_string == "":
        return 0
    else:
        for letter in input_string:
            if letter.isupper():
                counter += 1
    return counter


"""Count odds and evens."""


def count_odds_and_evens(numbers: list) -> str:
    r"""
    Return how many odd and even numbers are in the list.

    The task is to count how many odd and even numbers does the given list contain.
    Result should be displayed as string "ODDS: {number of odds}
                                          EVENS: {number of evens}"

    (the second line does not have any spaces before EVENS)

    count_odds_and_evens([1, 2, 3]) => "ODDS: 2\nEVENS: 1" (\n represents new line)
    count_odds_and_evens([1, 3]) => "ODDS: 2\nEVENS: 0" (\n represents new line)

    :param numbers: int
    :return: str
    """
    evens = 0
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    return f'ODDS: {len(numbers) - evens}\nEVENS: {evens}'


"""Close far."""


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if abs(b - a) <= 1 and (abs(c - a) >= 2 and abs(c - b) >= 2):
        return True
    elif abs(c - a) <= 1 and (abs(c - a) <= 2 and abs(c - b) <= 2):
        return True
    else:
        return False


"""Sum elements between 2 and 5."""


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5

    :param numbers:
    :return:
    """
    result = 0
    start_summing = False
    for number in numbers:
        if number == 2:
            start_summing = True
            continue
        if number == 5:
            start_summing = False
        if start_summing:
            result += number
    return result

    # for number in numbers:
    #     if start_summing and number != 5:
    #         result += number
    #     elif start_summing:
    #         start_summing = False
    #     if number == 2:
    #         start_summing = True
    # return result


if __name__ == '__main__':
    print(sum_between_25([1, 3, 6, 7]))
    print(sum_between_25([1, 2, 3, 4, 5, 6]))
    print(sum_between_25([1, 2, 3, 4, 6, 6]))
    print(sum_between_25([1, 3, 3, 4, 5, 6]))
    print(sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]))
    print(sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]))
    assert camel_case_word_counter("hello") == 1
    assert camel_case_word_counter("") == 0
    assert camel_case_word_counter("someMoreWordsHere") == 4

    assert count_odds_and_evens([1, 2, 3]) == "ODDS: 2\nEVENS: 1"
    assert count_odds_and_evens([1, 3]) == "ODDS: 2\nEVENS: 0"

    assert close_far(1, 2, 10) == True
    assert close_far(1, 2, 3) == False
    assert close_far(4, 1, 3) == True
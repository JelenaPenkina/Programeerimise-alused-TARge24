def bronze_coins_sum(coins):
    """
    Calculates the sum of all bronze coins.

    :param coins:
    :return: sum of bronze coins
    """
    sum_of_bronze_coins = sum(x for x in coins if x <= 5)
    return sum_of_bronze_coins


def ask_for_user_input():
    """
    Ask users for input fail name where is list of coins.

    :return: sum of bronze coins
    """
    file_input = input('Enter a file name where are list of coins: ')
    with open(file_input + '.txt', 'r') as f:
        coins_array = list(map(int, f.readlines()))
        print(f'All coins {coins_array}')
        return f'Sum of bronze coins is {bronze_coins_sum(coins_array)} cents'


if __name__ == '__main__':
    print(ask_for_user_input())
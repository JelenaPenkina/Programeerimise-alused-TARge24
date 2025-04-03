"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount
        self.earnings_per_day_cache = None

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        if self.earnings_per_day_cache is None:
            self.earnings_per_day_cache = (self.current_amount - self.starting_amount) / self.account_age
        return self.earnings_per_day_cache

    def belongs_to_bank(self, bank_name: str) -> bool:
        """Return true if this client belongs to a bank_name is a given bank_name."""
        return bank_name == self.bank


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    result = []
    with open(filename) as file:
        for line in file:
            first_name, bank_name, account_age, start_amount, current_amount = line.rstrip().split(",")
            result.append(Client(first_name, bank_name, int(account_age),
                                 int(start_amount), int(current_amount)))
    return result


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    return list(filter(lambda client: client.belongs_to_bank(bank), read_from_file_into_list(filename)))


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    client_list = read_from_file_into_list(filename)
    biggest_earner = max(client_list, key=lambda client: client.earnings_per_day())
    if biggest_earner.earnings_per_day() <= 0:
        return None
    biggest_earners = list(
        filter(lambda client: client.earnings_per_day() == biggest_earner.earnings_per_day, client_list))
    return sorted(biggest_earner, key=lambda client: client.account_age)[0]


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    client_list = read_from_file_into_list(filename)
    largest_loss = min(client_list, key=lambda client: client.earnings_per_day())
    if largest_loss.earnings_per_day() <= 0:
        return None
    largest_losses = list(filter(lambda client: client.earnings_per_day() == largest_loss.earnings_per_day(), client_list))
    return sorted(largest_loss, key=lambda client: client.account_age())[0]


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz

"""If you're going to perform inception, you need imagination."""


def countdown(n: int):
    """
    Write a simple recursive function that returns a list of numbers that count down from n.

    countdown(5) -> [5, 4, 3, 2, 1, 0]
    countdown(8) -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    countdown(-1) -> []

    :param n: start
    :return: countdown sequence
    """
    if n >= 0:
        return [n] + countdown(n - 1)
    return []


def add_commas(n: int):
    """
    In representing large numbers, from the right side to the left.

    English texts usually use commas to separate each group of three digits in front of the decimal.
    Your challenge is to output a number n formatted with commas.

    add_commas(1245) -> '1,245'
    add_commas(123456789) -> '123,456,789'
    add_commas(1011) -> '1,011'

    :param n: int
    :return: string of the formatted int
    """
    if len(str(n)) <= 3:
        return str(n)
    index = str(n)[-3:]
    return add_commas(str(n)[:-3]) + "," + index


def stonks(coins, rate, years):
    """
    Each year your crypto-investment grows.

    Write a recursive function that calculates the net worth of coins after some years.
    Rate is in percents.
    Round the answer down to the nearest integer.

    stonks(1000, 10, 10) -> 2593
    stonks(100000, 12, 3) -> 140492

    :param coins: starting amount (0-100000)
    :param rate: starting amount (0-100)
    :param years: starting amount (0-50)
    :return: coins after years
    """
    if rate == 0 or years == 0:
        return int(coins)
    return round(stonks(coins + (rate / 100 * coins), rate, years - 1))


def quic_mafs(a: int, b: int):
    """
    Write a recursive function that applies the following operations.

    i) If a=0 or b=0, return [a,b]. Otherwise, go to step (ii);
    ii) If a>=2*b, set a = a-2*b, and repeat step (i). Otherwise, go to step (iii);
    iii) If b>=2*a, set b = b-2*a, and repeat step (i). Otherwise, return [a,b].

    quic_mafs(6, 19) -> [6, 7]
    quic_mafs(2, 1) -> [0, 1]
    quic_mafs(22, 5) -> [0, 1]
    quic_mafs(8796203,7556) -> [1019,1442]

    :param a: int
    :param b: int
    :return: result
    """
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        return quic_mafs(a - 2 * b, b)
    elif b >= 2 * a:
        return quic_mafs(a, b - 2 * a)
    else:
        return [a, b]


def sum_squares(nested_list):
    """
    Write a function that sums squares of numbers in list.

    That list may contain additional lists.
    (Hint use the type() or isinstance() function)

    sum_squares([1, 2, 3]) -> 14
    sum_squares([[1, 2], 3]) -> sum_squares([1, 2]) + 9 -> 1 + 4 + 9 -> 14
    sum_squares([[[[[[[[[2]]]]]]]]]) -> 4

    :param nested_list: list of lists of lists of lists of lists ... and ints
    :return: sum of squares
    """
    if type(nested_list) is list:
        if len(nested_list) <= 0:
            return 0
        else:
            return sum_squares(nested_list[0]) + sum_squares(nested_list[1:])
    elif type(nested_list) is not list:
        return nested_list ** 2


if __name__ == "__main__":
    print(countdown(5))  # -> [5, 4, 3, 2, 1, 0]
    print(countdown(8))  # -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(countdown(-1))  # -> []

    print(add_commas(1245))  # -> '1,245'
    print(add_commas(123456789))  # -> '123,456,789'
    print(add_commas(1011))  # -> '1,011'

    print(stonks(1000, 10, 10))  # -> 2593
    print(stonks(100000, 12, 3))  # -> 140492
    print(stonks(1000, 0, 10))  # -> 2593
    print(stonks(10, 10, 1))  # -> 2593

    print(quic_mafs(6, 19))  # -> [6, 7]
    print(quic_mafs(2, 1))  # -> [0, 1]
    print(quic_mafs(22, 5))  # -> [0, 1]
    print(quic_mafs(8796203, 7556))  # -> [1019, 1442]

    print(sum_squares([1, 2, 3]))  # -> 14
    print(sum_squares([[1, 2], 3]))  # -> 14
    print(sum_squares([[[[[[[[[2]]]]]]]]]))  # -> 4
    print(sum_squares([[[[[[[[[]]]]]]]]]))  # -> 4

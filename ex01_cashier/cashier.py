"""EX01 - Cashier."""


def coin_count(s):
    """
    Based on a given sum, calculate how many coins to give back.

    :param s: Sum entered
    :return: Amount of coins needed.
    """
    coins = [50, 20, 10, 5, 1]
    x = 0
    for i in range(5):
        q = coins[i]
        x = x + int(s / q)  # for s=9, loop until i=5, then x=1
        s = int(s % q)  # 9 % 5 = 4 - enter new s into x, comes 1+4=5
    return x


s = input("Enter a sum: ")
s = int(s)
print("Amount of coins needed: " + str(coin_count(s)))

# The int() method returns an integer object from any number or string.
# %  is Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand.
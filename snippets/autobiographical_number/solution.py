def is_autobiographical(number):
    """
    Check if number is autobiographical.
    An autobiographical number is a number of which first digit counts
    how many zeros are in the number, the second digit counts how many
    ones are in the number, and so on.
    For example, 1210 is an autobiographical number.
    """
    number = str(number)
    for index, amount in enumerate(number):
        if number.count(str(index)) != int(amount):
            return False
    return True


def is_autobiographical_minimized(number):
    """
    Minimized version of is_autobiographical function.
    """
    number = list(map(int, list(str(number))))
    return all(number.count(i) == digit for i, digit in enumerate(number))

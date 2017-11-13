def insert_operator(number, result):
    """
    Insert operator inside given number to achieve expected result.

    :param number: number on which the operation should be performed
    :param result: expected result as number
    :return: string representation of performed operation to achieve the result
    """
    number = str(number)

    for i in range(len(number)):
        for sign in ('+', '-', '*', '/'):
            try:
                operation = '{}{}{}'.format(number[:i], sign, number[i:])
                if eval(operation) == result:
                    return operation
            except (SyntaxError, ZeroDivisionError):
                pass

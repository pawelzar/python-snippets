"""
Your program must insert the correct operator (+, -, / or *) at the right index of an integer number N so that the resulting operation equals a given integer X.

The operation is always valid and the result is always an integer. Plus '+' and minus '-' are the only operators that can be inserted at index 0.

In each test, there is only one possible solution.

INPUT:
An integer N and an integer X, separated by spaces.

OUTPUT:
N with an operator +, -, * or / inserted between the letters so that the resulting operation equals X.

EXAMPLE:
Input
3034 64
Output
30+34
"""

from operator import add, sub, mul, floordiv

operators = {'+': add, '-': sub, '*': mul, '/': floordiv}

num, result = input().split()
for i in range(len(num)):
    a = 0 if i == 0 else int(num[:i])
    b = int(num[i:])
    for sign, action in operators.items():
        try:
            if action(a, b) == int(result):
                print('{0}{2}{1}'.format(a if a != 0 else '', num[i:], sign))
                break
        except ZeroDivisionError:
            pass

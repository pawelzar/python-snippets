The program:
Given a string composed of numbers and letters, you must output a string where every substring is repeated as many times as the number preceding it.
The given string always starts with a number and ends with letters.

INPUT:
Line 1: A string S composed of numbers and letters.

OUTPUT:
Line 1: A string R where every substring has been repeated as many times as the number preceding it.

CONSTRAINTS:
1 < S < 50

EXAMPLE:
Input
1a2b3c4d
Output
abbcccdddd


import re
print("".join(str(int(x)*y) for x,y in re.findall('(\d+)([^0-9]+)', input())))

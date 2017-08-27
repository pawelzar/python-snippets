"""
Your program must determine if a given string would be a safe password. Here, a password is considered safe if:
It contains at least 8 characters.
It contains at least 1 digit (0-9).
It contains at least 1 lowercase letter (a-z).
It contains at least 1 uppercase letter (A-Z).

INPUT:
Line 1: P a string containing a password.

OUTPUT:
Line 1: true if P is a safe password, false otherwise.

CONSTRAINTS:
0 < P.length < 100

EXAMPLE:
Input
11/12/1978
Output
false
"""

import re

s = ''.join(sorted(input()))
print(str(bool(len(s) > 7 and re.search('\d.*[A-Z].*[a-z]', s))).lower())
# no match because there can be other signs between digits and letters

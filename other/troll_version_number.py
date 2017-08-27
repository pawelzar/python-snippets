"""
As Terry Pratchett explains in Men At Arms:
'Trolls traditionally count like this: (...) one, two, three... many (...) many-one, many-two, many-three, many-many, many-many-one, many-many-two, many-many-three, many-many-many, many-many-many-one, many-many-many-two, many-many-many-three, LOTS.'

From there we can extrapolate the following extra rules:
- after LOTS comes LOTS-one then LOTS-two and so on
- after LOTS-many-many-many-three comes LOTS-LOTS, then LOTS-LOTS-one, and so on
- after LOTS-LOTS-LOTS-many-many-many-three comes LOTS-LOTS-LOTS-LOTS, then LOTS-LOTS-LOTS-LOTS-one and so on (because trolls' imagination only gets them so far)

Given a number, your program must simply output the troll version of it.

INPUT:
Line 1: a single number N

OUTPUT:
Line 1: the troll version of N

CONSTRAINTS:
1 ≤ N ≤ 1000

EXAMPLE:
Input
1
Output
one
"""

n = int(input())
out = ''
if n/16 >= 1:
    out += 'LOTS-' * int(n/16)
    n %= 16
if n/4 >= 1:
    out += 'many-' * int(n/4)
    n %= 4
if n > 0:
    out += ['one', 'two', 'three'][n-1]
print(out.rstrip('-'))

"""
You're given a string S, consisting only of lowercase Latin letters. Find whether it is possible to convert it into a palindrome by inserting only one character.

If it is possible, return the index (0-based Index) where the character should be inserted. If there is more than one, return the smallest one. If it is not possible, return -1.

INPUT:
A single line containing the word to transform S.

OUTPUT:
The index (0-based Index) where the character should be inserted or -1.

CONSTRAINTS:
1 ≤ length of S ≤ 100

EXAMPLE:
Input
aa
Output
0
"""

word = input()
i = 0
possible = False
while i <= len(word):
    t = ''
    for s in 'abcdefghijklmnopqrstuvwxyz':
        t = word[:i] + s + word[i:]
        if t == t[::-1]:
            possible = True
            break
    if possible:
        print(i)
        break
    else:
        i += 1
else:
    print(-1)

"""
Everytime Marco tries to speak, he stammers.
If Marco has to say a text out loud, he will stammer on the first two letter of each word.

Here's the thing though, if he starts stammering, it will only get worse.
At first, he does not stammer.
Then, he stammers once.
When he's trying to say the nth word, he will stammer as many times as he did previously ((n-1)th word) plus as many times as he did even before that ((n-2)th word).
Input
One line: The string S that marco is trying to say
Output
One line: The sentence m that Marco will end up saying
Constraints
0 < length(s) < 100
Example
Input
Hi there
Output
Hi th-there
"""

sentence = input().split()
m = 0
n = 1
out = [sentence[0]]

if len(sentence) > 1:
    out.append(sentence[1][:2] + '-' + sentence[1])

for word in sentence[2:]:
    out.append((word[:2] + '-') * (m+n) + word)
    temp = n
    n += m
    m = temp

print(' '.join(out))

def squares_generator():
    """Generates number and its square, starting from 1."""
    number = 1
    while True:
        yield number
        yield number ** 2
        number += 1

sq = squares_generator()
for x in range(100):
    print "number %s" % sq.next()
    print "square %s" % sq.next()


def fibonacci_generator(n):
    """Generates Fibonacci Sequence."""
    prev = 0
    sequent = 1
    for num in range(n):
        yield prev
        act = prev
        prev = sequent
        sequent += act

fb = [x for x in fibonacci_generator(14)]
print fb


def split_generator(sentence, sign):
    """Generates words from sentence s, separated by x."""
    i = 0
    out = ""
    while i < len(sentence):
        k = sentence.find(sign, i)
        if k > 0:
            out = sentence[i:k]
            i = k + len(sign)
            yield out
        else:
            out = sentence[i:]
            break
    yield out

a = split_generator('This is a sample sentence', 'is')
print a.next()
print a.next()
print a.next()

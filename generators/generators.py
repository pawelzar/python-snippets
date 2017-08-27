class Generator:

    @staticmethod
    def squares():
        """Generates number and its square, starting from 1."""
        number = 1
        while True:
            yield number
            yield number ** 2
            number += 1

    @staticmethod
    def fibonacci(n):
        """Generates Fibonacci Sequence."""
        prev = 0
        sequent = 1
        for num in range(n):
            yield prev
            act = prev
            prev = sequent
            sequent += act

    @staticmethod
    def split(sentence, sign):
        """Generates words from sentence, separated by given sign."""
        i = 0
        out = ''
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

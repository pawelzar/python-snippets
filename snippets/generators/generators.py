class Generator:
    """
    Basic generator class for common functions.
    """

    @staticmethod
    def squares():
        """
        Generates number and its square, starting from 1.
        """
        number = 1
        while True:
            yield number
            yield number ** 2
            number += 1

    @staticmethod
    def fibonacci(number):
        """
        Generates Fibonacci Sequence.
        """
        prev = 0
        sequent = 1
        for _ in range(number):
            yield prev
            temp = prev
            prev = sequent
            sequent += temp

    @staticmethod
    def split(sentence, sign=' '):
        """
        Generates words from sentence separated by given sign.

        :param sentence: text of any length
        :param sign: string separator
        :return: list of words separated by separator
        """
        index = 0
        word = ''
        while index < len(sentence):
            next_occurrence = sentence.find(sign, index)
            if next_occurrence > 0:
                word = sentence[index:next_occurrence]
                index = next_occurrence + len(sign)
                yield word
            else:
                word = sentence[index:]
                break
        yield word

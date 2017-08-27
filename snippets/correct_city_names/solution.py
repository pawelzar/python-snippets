def correct_names(correct, incorrect):
    """
    Correct wrongly written names according to provided list of correct names.

    :param correct: list of names that are written correctly
    :param incorrect: list of names that are written incorrectly
    :return: list of corrected names
    """
    normalized = {normalize(name): name for name in correct}
    return [normalized.get(normalize(name), '') for name in incorrect]


def normalize(name):
    """
    Return lowercase name without spaces.
    """
    return name.lower().replace(' ', '')


if __name__ == '__main__':
    correct = [input() for i in range(int(input()))]
    incorrect = [input() for i in range(int(input()))]

    print('\n'.join(correct_names(correct, incorrect)))

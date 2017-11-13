from string import ascii_lowercase


def insert_to_palindrom(word):
    """
    Checks if it is possible to create a palindrom by adding only one letter.

    :param word: string consisting of lowercase Latin letters
    :return: index at which letter should be inserted or -1 if not possible
    """
    for i in range(len(word)):
        for letter in ascii_lowercase:
            new_word = word[:i] + letter + word[i:]
            if new_word == new_word[::-1]:
                return i
    return -1

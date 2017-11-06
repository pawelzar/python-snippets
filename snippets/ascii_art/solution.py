from string import ascii_uppercase


def ascii_art(width, height, art, text):
    """
    Represent text in ASCII art.

    :param width: width of single element in ASCII art
    :param height: height of single element in ASCII art
    :param art: alphabet in ASCII art represented as several lines of strings
    :param text: string that is going to be represented in ASCII art
    :return: text converted to list of strings in ASCII art
    """
    text_in_art = [''] * height

    for sign in text.upper():
        if sign in ascii_uppercase:
            start = ascii_uppercase.index(sign) * width
            for line in range(height):
                text_in_art[line] += art[line][start:start + width]
        else:
            for line in range(height):
                # represent unknown character as '?' (last sign in given art)
                text_in_art[line] += art[line][-width:]

    return text_in_art


if __name__ == '__main__':
    WIDTH = int(input())
    HEIGHT = int(input())
    TEXT = input()
    ART = [input() for i in range(HEIGHT)]

    print('\n'.join(ascii_art(WIDTH, HEIGHT, ART, TEXT)))

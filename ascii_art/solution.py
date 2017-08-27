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
        if ord(sign) in range(65, 91):  # uppercase letters in ASCII
            for line in range(height):
                start = (ord(sign) - 65) * width
                end = ((ord(sign) - 65) + 1) * width
                text_in_art[line] += art[line][start:end]
        else:
            for line in range(height):
                # represent character as '?' (last sign in provided art)
                # if it wasn't recognized
                text_in_art[line] += art[line][26 * width:]

    return text_in_art

if __name__ == '__main__':
    width = int(input())
    height = int(input())
    text = input()
    art = [input() for i in range(height)]

    print('\n'.join(ascii_art(width, height, art, text)))

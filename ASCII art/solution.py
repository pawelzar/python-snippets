def ascii_art(width, height, text, art):
    """Returns text represented in ASCII art."""
    text_in_art = [""] * height

    for sign in text.upper():
        if ord(sign) in range(65, 91):
            for line in range(height):
                start = (ord(sign)-65) * width
                end = ((ord(sign) - 65) + 1) * width
                text_in_art[line] += art[line][start: end]
        else:
            for line in range(height):
                text_in_art[line] += art[line][26 * width: 27 * width]

    return text_in_art

if __name__ == "__main__":
    l = int(input())
    h = int(input())
    text = input().upper()

    art = [input() for i in range(h)]
    output = [""] * h

    for char in text:
        if ord(char) in range(65, 91):
            for line in range(h):
                output[line] += art[line][(ord(char)-65)*l: ((ord(char)-65)+1)*l]
        else:
            for line in range(h):
                output[line] += art[line][26*l: 27*l]

    for row in output:
        print(row)

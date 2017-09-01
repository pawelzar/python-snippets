def slide_down(array):
    """
    Pushes each element different than '.' to the bottom of proper column.

    :param array: two dimensional array
    :return: list of strings representing array with elements slided down
    """
    height = len(array)
    lines = [''.join(line) for line in zip(*array)]

    for i, line in enumerate(lines):
        lines[i] = line.replace('.', '').ljust(height, '.')[::-1]

    return [''.join(line) for line in zip(*lines)]


if __name__ == '__main__':
    WIDTH, HEIGHT = [int(i) for i in input().split()]
    ARRAY = [input() for i in range(HEIGHT)]

    print('\n'.join(slide_down(ARRAY)))

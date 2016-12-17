def slide_down(art):
    """Returns map with elements != '.' pushed to the bottom in each column."""
    height = len(art)
    lines = ["".join(x) for x in zip(*art)]

    for i, line in enumerate(lines):
        lines[i] = line.replace(".", "").ljust(height, ".")[::-1]

    return ["".join(line) for line in zip(*lines)]


if __name__ == '__main__':
    width, height = [int(i) for i in input().split()]
    lines = ["".join(x) for x in zip(*[input() for i in range(height)])]

    for i, line in enumerate(lines):
        lines[i] = line.replace(".", "").ljust(height, ".")[::-1]

    for line in zip(*lines):
        print("".join(line))

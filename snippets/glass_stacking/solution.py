def glass_stack(number):
    """
    Returns art composed of glasses stacked on top of each other
    in a triangular shape.
    Provided parameter is the maximum number of glasses that can be used
    to form a stack.
    """
    count = 0
    height = 0
    glasses = []

    while count + height < number:
        height += 1
        count += height

    for i in range(1, height + 1):
        for line in [' ***  ', ' * *  ', ' * *  ', '***** ']:
            glasses.append('{:^{}}'.format(line * i, height * 6)[:-1])

    return glasses


if __name__ == '__main__':
    n = int(input())
    print('\n'.join(glass_stack(n)))

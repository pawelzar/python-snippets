def glass_stack(glasses):
    """
    Composes stack of glasses in triangular shape.

    :param glasses: the maximum number of glasses that can be used to
    form a stack
    :return: list of strings representing glasses stacked on top of each other
    in a triangular shape
    """
    glass = [
        ' ***  ',
        ' * *  ',
        ' * *  ',
        '***** ',
    ]
    stack = []
    stack_tiers = 0
    used_glasses = 0

    # stack_tiers + 1 = number of glasses in next tier
    while used_glasses + stack_tiers < glasses:
        stack_tiers += 1
        used_glasses += stack_tiers

    for tier in range(1, stack_tiers + 1):
        for line in glass:
            stack.append('{:^{}}'.format(line * tier, stack_tiers * 6)[:-1])

    return stack


if __name__ == '__main__':
    GLASSES = int(input())

    print('\n'.join(glass_stack(GLASSES)))

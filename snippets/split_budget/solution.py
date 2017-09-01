def split_budgets(budgets, gift):
    """
    Divide gift price as even as possible.

    :param budgets: list of individual budgets
    :param gift: gift price
    :return: list of evenly divided shares
    """
    if sum(budgets) < gift:
        return 'IMPOSSIBLE'

    division = []
    quantity = len(budgets)

    for money in sorted(budgets):  # start from the smallest limit
        if money < gift / quantity:
            gift -= money
            division.append(money)
        else:
            division.append(int(gift / quantity))
            gift -= int(gift / quantity)
        quantity -= 1

    return division

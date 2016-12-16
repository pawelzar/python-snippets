def split_budgets(budget, gift):
    """
    Divide gift price as even as possible.
    Returns list of shares for each budget.
    """
    if sum(budget) < gift:
        return "IMPOSSIBLE"
    else:
        division = []
        quantity = len(budget)

        for money in sorted(budget):  # start from the smallest limit
            if money < gift / quantity:
                gift -= money
                division.append(money)
            else:
                division.append(int(gift / quantity))
                gift -= int(gift / quantity)
            quantity -= 1

        return division

def is_balanced(sequence):
    """CHeck if brackets in given sequence are properly closed."""
    brackets = "([{)]}"
    stack = []

    for a in input():
        if a in brackets[:3]:
            stack.append(brackets.index(a))
        elif a in brackets[3:]:
            if not (len(stack) > 0 and stack.pop() == brackets.index(a) % 3):
                return False
    else:
        return bool(not stack)

def is_balanced(sequence):
    """
    Check if brackets in given sequence are properly closed.
    """
    brackets = '([{)]}'
    stack = []

    for char in sequence:
        if char in brackets[:3]:
            stack.append(brackets.index(char))
        elif char in brackets[3:]:
            if not (stack and stack.pop() == brackets.index(char) % 3):
                return False
    return not stack

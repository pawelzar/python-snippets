def is_autobiographical(number):
    x = str(number)
    for i, digit in enumerate(x):
        if not x.count(str(i)) == int(digit):
            return False
    else:
        return True


def is_autobiographical_2(number):
    s = map(int, list(str(number)))
    return bool(all(s.count(i) == num for i, num in enumerate(s)))

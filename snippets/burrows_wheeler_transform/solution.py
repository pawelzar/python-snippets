def bw_transform(word):
    """
    Compute the Burrows-Wheeler transform of the given string.
    """
    cycles = []
    for index, char in enumerate(word):
        char_position = word.index(char, index)
        cycles.append(word[char_position:] + word[:char_position])
    cycles.sort()
    bw_index = cycles.index(word) + 1  # count from 1
    bw_string = ''.join(list(zip(*cycles))[-1])
    return '{}{}'.format(bw_index, bw_string)


def bw_transform_minimized(word):
    """
    Minimized version of bw_transform function.
    """
    new = sorted(word[len(word)-i-1:] + word[:len(word)-i-1]
                 for i in range(len(word)))
    return str(new.index(word)+1) + ''.join(w[len(word)-1] for w in new)

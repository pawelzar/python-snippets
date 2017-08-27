def bw_transform(word):
    cycles = []
    for i, c in enumerate(word):
        cycles.append(
            word[word.index(c, i):] + word[:word.index(c, i)])
    cycles.sort()
    return str(cycles.index(word)+1) + ''.join(w[len(word)-1] for w in cycles)


def bw_transform_2(word):
    new = sorted(word[len(word)-i-1:] + word[:len(word)-i-1]
                 for i in range(len(word)))
    return str(new.index(word)+1) + ''.join(w[len(word)-1] for w in new)

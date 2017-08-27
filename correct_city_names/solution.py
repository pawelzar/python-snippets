def correct_names(well_written, bad_written):
    """Returns list of corrected names."""
    pattern = {"".join(name.lower().split()): name for name in well_written}

    corrected_names = []
    for name in bad_written:
        corrected_name = pattern["".join(name.lower().split())]
        corrected_names.append(corrected_name)

    return corrected_names


if __name__ == "__main__":
    correct = {}
    for i in range(int(input())):
        word = input()
        correct["".join(word.lower().split())] = word

    incorrect = [input() for i in range(int(input()))]
    for word in incorrect:
        print(correct["".join(word.lower().split())])

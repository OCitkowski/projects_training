def high(x):
    abc_string = 'abcdefghijklmnopqrstuvwxyz'
    word_dict2 = [sum([abc_string.index(j) + 1 for j in i]) for i in x.split(" ")]

    return x.split(" ")[word_dict2.index(max(word_dict2))]


def high_best(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

if __name__ == '__main__':
    assert high('man i need a taxi up to ubud') == 'taxi'

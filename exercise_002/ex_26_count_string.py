from collections import Counter


def count(string):
    count = Counter(string)
    result = {}
    for i in set(string):
        result[i] = count[i]
    # print(result)
    return result

#
# from collections import Counter
#
# def count(string):
#     return Counter(string)


if __name__ == '__main__':
    count('aba')  #{'a': 2, 'b': 1}
    assert(count('aba') == {'a': 2, 'b': 1})
    assert(count('') == {})


def array_diff(a: list, b: list) -> list:

    if len(b) == 0:
        return a

    for i in range(0, len(b)):
        while True:
            if b[i - 1] in a:
                a.remove(b[i - 1])
            else:
                break

    if __name__ == '__main__':
        print(a)
    return a

def best_array_diff(a, b):
    return [x for x in a if x not in b]

if __name__ == '__main__':

    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 3], [1, 2]) == [3]
    assert array_diff([1, 2, 2], [2]) == [1]



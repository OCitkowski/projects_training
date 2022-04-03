def unique_in_order(iterable):

    new_iterable = []
    if int(len(iterable)) == 0:
        return new_iterable
    new_iterable.append(iterable[0])
    [new_iterable.append(i) for i in iterable[1:] if len(new_iterable) > 0 and new_iterable[-1] != i]
    return new_iterable


def best_unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

if __name__ == '__main__':
    print(unique_in_order([1, 2, 2, 3, 3, 5, 5, 111]))
    print(unique_in_order('ABBCcAD'))
    assert unique_in_order([1, 2, 2, 3, 3, 5, 5, 111]) == [1, 2, 3, 5, 111]
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
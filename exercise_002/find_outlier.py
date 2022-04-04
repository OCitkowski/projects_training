def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0]
    odd = [i for i in integers if i % 2 != 0]
    if len(even) > len(odd):
        # print(f'{odd[0]}')
        return odd[0]
    else:
        # print(f'{even[0]}')
        return even[0]

def bestpr_find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

if __name__ == '__main__':
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
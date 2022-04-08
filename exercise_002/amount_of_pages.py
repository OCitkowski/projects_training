def best_amount_of_pages(summary):
    # 1-9:          9       = 9 * 1 * 10**0
    # 10-99:        180     = 9 * 2 * 10**1
    # 100-999:      2700    = 9 * 3 * 10**2
    # 1000-9999:    36000   = 9 * 4 * 10**3
    # 10000-99999:  450000  = 9 * 5 * 10**4
    res = 0
    for x in range(1, 6):
        y = 9 * x * 10**(x-1)
        if summary <= y:
            return res + summary//x
        res += y//x
        summary -= y

def amount_of_pages(summary: int, len_sum: int = None) -> int:
    calculate_old = lambda num: (len(''.join([str(i) for i in range(1, num + 1)])))
    calc_string = f'({summary}'
    len_sum = len(str(summary)) if len_sum == None else len_sum
    for i in range(0, len_sum):
        if i != len_sum - 1:
            calc_string += ' - '
            calc_string += '9' + '0' * i + '*' + f'{i + 1}'
        else:
            if len_sum == 1:
                calc_string += ')'
            else:
                calc_string += f') // {len_sum} + {"9" * (len_sum - 1)}'
    result = eval(calc_string)

    if summary != calculate_old(result):
        result = amount_of_pages(summary, len_sum - 1)

    print(f'{calc_string} ----- res {result} // sum {summary} == {calculate_old(result)}')
    return result

if __name__ == '__main__':
    # amount_of_pages(1095)
    # assert amount_of_pages(5) == 5
    assert amount_of_pages(25) == 17
    assert amount_of_pages(185) == 97
    assert amount_of_pages(660) == 256
    assert amount_of_pages(1095) == 401
    assert amount_of_pages(2893) == 1000

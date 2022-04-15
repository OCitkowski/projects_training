def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum_num, sum_str = 0, ''

    for i in range(len(roman), 0, -1):
        index = i - 1

        if len(roman) == i:
            sum_num += numeral[roman[index]]
            # sum_str += f'{numeral[roman[index]]}'
        elif numeral[roman[index]] < numeral[roman[index + 1]]:
            sum_num -= numeral[roman[index]]
            # sum_str += f' - {numeral[roman[index]]}'
        else:
            sum_num += numeral[roman[index]]
            # sum_str += f' + {numeral[roman[index]]}'

    # print(f' sum_num = {sum_num} sum_str = {sum_str}')
    return sum_num

values = [('M', 1000), ('CM', -200), ('D', 500), ('CD', -200),
          ('C', 100), ('XC', -20), ('L', 50), ('XL', -20),
          ('X', 10), ('IX', -2), ('V', 5), ('IV', -2),
          ('I', 1)]
def best_solution(roman):
    return sum(roman.count(s)*v for s,v in values)


if __name__ == '__main__':
    solution('IX')
    # assert solution('XXI') == 21
    # assert solution('III') == 3
    # assert solution('XXVI') == 26
    # assert solution('XXIV') == 24
    # assert solution('I') == 1
    # assert solution('X') == 10
    # assert solution('MMVIII') == 2008
    # assert solution('MDCLXVI') == 1666
    # assert solution('XLIV') == 44
    # assert solution('MCMXCIX') == 1999
    # assert solution('MCDXCIX') == 1499

    # Symbol    Value
    # I          1
    # V          5
    # X          10
    # L          50
    # C          100
    # D          500
    # M          1,000

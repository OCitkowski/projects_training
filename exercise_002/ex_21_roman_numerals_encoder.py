# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral
# representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit
# and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC;
# resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending
# order: MDCLXVI.

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(n):
    # TODO convert int to roman string
    roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    return 'I'


if __name__ == '__main__':
    assert solution(1) == 'I'
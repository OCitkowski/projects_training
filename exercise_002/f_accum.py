# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
#
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# best practic
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# def accum(s):
#
#     i, result = 0, ''
#
#     while i < len(s):
#         result += f'{(s[i] * (i + 1)).capitalize()}-'
#         i += 1
#     return result[:-1]

if __name__ == '__main__':

    print(f'*** - {accum("ZpglnRxqenU")}')

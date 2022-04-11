# Task:
# You need to write a function grid that returns an alphabetical grid of size NxN, where a = 0, b = 1, c = 2....
# Examples:
# grid(4)
#
# a b c d
# b c d e
# c d e f
# d e f g
#
# After "z" comes "a"
# If function receive N < 0 should return:

# def grid(N):
#     N = int(N)
#     if N < 0:
#         return None
#
#     abc_string = 'abcdefghijklmnopqrstuvwxyz'
#     quantity = 3 * N // len(abc_string)
#     abc_fool = abc_string * (quantity + 1)
#     result = ''
#     i = 0
    #
    # while i != N:
    #     for letter in abc_fool[i: N + i]:
    #         result += f'{letter} '
    #     i += 1
    #     result = result[:-1]
    #     if i != N:
    #         result += f'\n'

    # result.join()
    #
    # return result

# best practic
def grid(N):
    if N < 0:
        return None
    abc = 'abcdefghijklmnopqrstuvwxyz' * 8 # Error  n = 1000???
    val = []
    for i in range(N):
        arr = list(abc[i: N+i])
        out = ' '.join(arr)
        val.append(out)
    return '\n'.join(val)

# print(grid(int(input('enter - '))))

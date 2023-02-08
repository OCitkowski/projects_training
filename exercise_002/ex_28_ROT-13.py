from string import ascii_letters

import string


def rot13_4(message):
    PAIRS = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))
    return "".join(PAIRS.get(c, c) for c in message)


def rot13_3(message):
    first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    return message.translate(string.maketrans(first, trance))


def rot13_2(message):
    return message.encode('rot13')


def rot13(message):
    input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    res = {input[i]: output[i] for i in range(len(input))}
    result = ''
    for i in message:
        if i in output:
            result += res[i]
        else:
            result += i

    print(result)

    return result


def jjj():
    x = lambda a: a + 10
    print(x(5))


if __name__ == '__main__':
    # print(ascii_letters)
    jjj()
    axz = lambda a, x, z: (a + x) * z
    print(axz(5, 10, 2))

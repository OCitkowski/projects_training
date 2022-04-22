import string
from string import ascii_lowercase as l, ascii_uppercase as u


# >>> string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# >>> string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encryptor(key, message):

    result = ""
    n = abs(key) // 26

    if key >= 0:
        key -= n * 26
    else:
        key += (n + 1) * 26

    for letter in message:

        if letter in string.ascii_lowercase:
            index_letter = string.ascii_lowercase.find(letter)
            index_letter_key = index_letter + key
            lower = True
        elif letter in string.ascii_uppercase:
            index_letter = string.ascii_uppercase.find(letter)
            index_letter_key = index_letter + key
            lower = False
        else:
            result += letter
            continue

        if index_letter_key > 25:
            n_key = index_letter_key // 26
            index_letter_key = index_letter_key - n_key * 26

        if lower:
            result += string.ascii_lowercase[index_letter_key]
        else:
            result += string.ascii_uppercase[index_letter_key]

#     print(f'"{result}" "{message}"')

    return result

def best_encryptor(key, message):
    process = lambda x, abc: x in abc and abc[(abc.index(x) + key) % 26]
    return ''.join(process(c, l) or process(c, u) or c for c in message)

def gg(key):

    process = lambda x, abc: x in abc and abc[(abc.index(x) + key) % 26]
    return process(l, u)

if __name__ == '__main__':
    print(gg(25))
    # best_encryptor(-39, 'Too Many Cooks.')
    # encryptor( 0, 'Too Many Cooks.')
    # encryptor( 26, 'Too Many Cooks.')
    # encryptor( -1, 'Too Many Cooks.')
    # encryptor( 100, 'Too Many Cooks.')
    # assert encryptor(13, 'Caesar Cipher') == 'Pnrfne Pvcure'



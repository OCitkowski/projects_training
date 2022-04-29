# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

def is_valid_IP_my(strng):
    # x = '.'
    # h = [x.join(i) for i in strng.split(".")]
    # for i in strng.split("."):
    #     print(i)
    #     h = x.join(i)

    # print(x, h, strng.split("."))
    #
    # a = ['red', 'green', 'blue']
    #
    # print(' '.join(a))
    # print(''.join(a))
    # print('***'.join(a))
    #
    # a =  'blue'
    #
    # print(' '.join(a))
    # print(''.join(a))
    # print('***'.join(a))
    result = False
    # print(f'{strng.split(".")}   {"" in strng.split(".")}')
    if len(strng.split(".")) == 4 and ''.join(strng.split(".")).isdigit() and not ("" in strng.split(".")):

        left = [int(i) for i in strng.split(".") if len(strng) > 0]
        right = [int(i) for i in strng.split(".") if i.isdigit() and str(int(i)) == i and i.isdigit() and int(i) < 256 and len(i) != 0]
        result = left == right
    return result

if __name__ == '__main__':

    # assert is_valid_IP('12.255.56.1') == True
    # assert is_valid_IP('') == False
    # assert is_valid_IP('12.255.056.1') == False
    # assert is_valid_IP('12.255.56.1.5') == False
    # assert is_valid_IP('12.255.56') == False
    # assert is_valid_IP('12.rrr.56') == False


    assert is_valid_IP('12.255..1') == False
    assert is_valid_IP('abc.def.ghi.jkl') == False


    # is_valid_IP('78.065')
    # is_valid_IP('')
    # is_valid_IP('12.255.56.1')


# def split_string(string: str) -> list:
#     if string == '':
#         return None
#
#     if (len(string) % 2) > 0:
#         string += '_'
#
#     result = []
#     i = 1
#     element = ''
#     for symbol in string:
#         element += symbol
#         i += 1
#         if i > 2:
#             result.append(element)
#             element = ''
#             i = 1
#     return result


def scrolling_text(string: str) -> list:
    result = []
    list_string = list(string)

    for i in range(0, len(list_string)):
        new_string = ''.join(list_string).upper()
        result.append(new_string)
        x = list_string.pop(0)
        list_string.append(x)
    return result

def check_number(number: int) -> list:
    result = []

    if number > 0:
        result.append(True)
    else:
        result.append(False)

    if number % 2 == 0:
        result.append(True)
    else:
        result.append(False)

    if number % 10 == 0:
        result.append(True)
    else:
        result.append(False)

    return result




if __name__ == '__main__':
    print(check_number(3))  # [True, False, False]
    print(check_number(10))  # [True, True, True]
    print(check_number(0))  # [False, True, True]
    print(check_number(-1)) # [False, False, False]

    # print(split_string("123456"))  # ["12", "34", "56"]
    # print(split_string("ab cd ef"))  # ["ab", " c", "d ", "ef"]
    # print(split_string("abc"))  # ["ab", "c_"]
    # print(split_string(" "))  # [" _"]
    # print(split_string(""))  #

    # print(scrolling_text('robot'))

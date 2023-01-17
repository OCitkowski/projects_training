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


def combine_lists(ls1: list, ls2: list) -> list:
    ls = []
    for i in range(len(ls1)):
        ls.append(ls1[i] + ls2[i])
    return ls


def is_jumping(number: int) -> str:
    numbers_list = list(str(number))
    result = 'JUMPING'
    for i in range(len(numbers_list)):
        if i == 0:
            continue
        x = int(numbers_list[i])
        x1 = int(numbers_list[i - 1])

        if (x - x1) == -1 or (x - x1) == 1:
            continue
        else:
            result = 'NOT JUMPING'
            break

    return result


def is_special_number(number: int) -> str:
    numbers_list = list(str(number))
    result = "Special!!"
    for i in range(len(numbers_list)):
        if int(numbers_list[i]) in (0, 1, 2, 3, 4, 5):
            continue
        else:
            result = "NOT!!"
            break
    return result


def is_tidy(number: int) -> bool:
    numbers_list = list(str(number))
    result = True
    for i in range(len(numbers_list)):
        if i == 0:
            continue
        x = int(numbers_list[i])
        x1 = int(numbers_list[i - 1])

        if x >= x1:
            continue
        else:
            result = False
            break

    return result

def get_largest_expression_result(a, b):

    # the_bigest = []
    # the_bigest.append(a + b)
    # the_bigest.append(a - b)
    # the_bigest.append(a * b)
    # the_bigest.append(a / b)
    #
    # the_bigest = sorted(the_bigest)
    #
    # return the_bigest[3]

    for i in range('klghjkghjl'):
        print(i)





if __name__ == '__main__':
    print(get_largest_expression_result(10, 5))  # 50
    print(get_largest_expression_result(10, -5))  # 15
# # Число з однієї цифри
# print(is_jumping(98))  # "JUMPING"
# # 7 і 9 відрізняються на 2, а не на 1
# print(is_jumping(78))  # "NOT JUMPING"
# # Різниця між однаковими цифрами дорівнює 0
# print(is_jumping(7889))  # "NOT JUMPING"
# # Усі сусідні цифри відрізняються на 1
# print(is_jumping(23454))  # "JUMPING

# print(combine_lists([1, 2, 5], [3, 6, 1]))  # [4, 8, 6]
# print(combine_lists([1], [6]))  # [7]
# print(combine_lists([], [])) # []

# print(check_number(3))  # [True, False, False]
# print(check_number(10))  # [True, True, True]
# print(check_number(0))  # [False, True, True]
# print(check_number(-1)) # [False, False, False]

# print(split_string("123456"))  # ["12", "34", "56"]
# print(split_string("ab cd ef"))  # ["ab", " c", "d ", "ef"]
# print(split_string("abc"))  # ["ab", "c_"]
# print(split_string(" "))  # [" _"]
# print(split_string(""))  #

# print(scrolling_text('robot'))

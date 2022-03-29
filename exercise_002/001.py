# Dot Calculator
#
# You have to write a calculator that receives strings for input. The dots will represent the number in the equation.
# There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be
# separated by one space.
#
# Here are the following valid operators :
#
#     + Addition
#     - Subtraction
#     * Multiplication
#     // Integer Division
#
# Your Work (Task)
#
# You'll have to return a string that contains dots, as many the equation returns. If the result is 0,' \
#    ' return the empty string. When it comes to subtraction, the first number will always be greater ' \
#    'than or equal to the second number.
#
# Examples (Input => Output)
# * "..... + ..............." => "...................."
# * "..... - ..."             => ".."
# * "..... - ."               => "...."
# * "..... * ..."             => "..............."
# * "..... * .."              => ".........."
# * "..... // .."             => ".."
# * "..... // ."              => "....."
# * ". // .."                 => ""
# * ".. - .."                 => ""
# my solution
def calculator(txt):
    txt = txt.replace(' ', '')
    if txt.find('+') >= 1:
        list_input = txt.split('+')
        result_quantity = len(list_input[0]) + len(list_input[1])
        result = '.' * result_quantity

    elif txt.find('-') >= 1:
        list_input = txt.split('-')
        result_quantity = len(list_input[0]) - len(list_input[1])
        if result_quantity < 0:
            result_quantity = 0
        result = '.' * result_quantity

    if txt.find('*') >= 1:
        list_input = txt.split('*')
        result_quantity = len(list_input[0]) * len(list_input[1])
        result = '.' * result_quantity

    if txt.find('//') >= 1:
        list_input = txt.split('//')
        result_quantity = len(list_input[0]) // len(list_input[1])
        result = '.' * result_quantity

    return result

#  best solution
def calculator2(txt):
    a, op, b = txt.split()
    a, b = len(a), len(b)
    return '.' * eval(f'{a} {op} {b}')

#  best solution2

my_entry = input('entry - ')
print(calculator(my_entry))
print(calculator2(my_entry))


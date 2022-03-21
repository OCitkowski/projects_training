import json


def write_in_file_json(numbers):
    file_name = 'numbers.json'
    try:
        with open(file_name, "a") as my_file:
            json.dump(numbers, my_file)
    except:
        with open(file_name, "x") as my_file:
            json.dump(numbers, my_file)
        # print("Sory? We don`t have file.")
    else:
        print(f" is good")

def read_in_file_json(numbers):
    file_name = 'numbers.json'
    try:
        with open(file_name, "a") as my_file:
            json.dump(numbers, my_file)
    except:
        with open(file_name, "x") as my_file:
            json.dump(numbers, my_file)
        # print("Sory? We don`t have file.")
    else:
        print(f" is good")

def print_my_file(file_name):

    with open(file_name) as my_file:
        for row in my_file:
            if len(row) != 1:
                # print(len(row))
                print(f"{len(row)} {row.rstrip()}")

def rewrite_my_file(file_name):
    with open(file_name, 'a') as my_file:
        my_file.write(f'\n{input("input row") * 6}')

def zero_division(numerator, denominator,  response):
    try:
        answer = numerator/denominator
        print(f'{answer}')
    except:
        print(f'{response}')
        answer = None
    else:
        print(f'run else')
        answer = None
    return answer


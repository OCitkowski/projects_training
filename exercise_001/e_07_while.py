# index = input('How long is this')
# if type(index) != "int":
#     index = int(index)
# my_dict = {}
# while index != 0:
#     index -= 1
#     name = input('Please enter yor name -')
#     age = input('How old this man')
#     my_dict[name] = int(age)
#
# print(f'{my_dict}')
# *******************7.1***********************************
active = True
my_dict = {}
while active:
    name = input('Please enter your name - \n')
    age = input('Please enter how your old - \n')

    if name == None or age == None:
        break
    elif len(name) <= 2:
        continue
    elif int(age) < 10 or int(age) > 100:
        print( f" This is false - {age} year. Please enter your age - ")
    else:
        my_dict[name] = age

print(my_dict)


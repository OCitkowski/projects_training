from builtins import print

a = 1111
b = 2222
a, b = b, a
my_list = list("dfgfdgfd")
print(my_list)

if "d" in my_list:
    print(f' d in {my_list}')
if 'hh' not in my_list:
    print(f' hh not in {my_list}')

if a == 1111 and b == 2222:
    print(f' a =1111  ****')
if a != 1111 and b != 2222:
    print( f' a = 2222 ****')
if a == 1111 or b == 1111:
    print(f' 1111 ****')

print(f" a- {a}, b- {b}")

# _age = int(input())
# if _age < 10:
#     print(f' {_age} < 10')
# elif _age < 100:
#     print(f' {_age} < 100')
# else:
#     print(f' XZ')

cars = ['audi', 'bmw', 'subaru', 'toyota']
print(type(cars))

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

my_list2 = []
my_tuple = ()
if not my_list2:
    print(f' my_list2 - {my_list2}')

if not my_tuple:
    print(f' {type(my_tuple)}my_tuple - {my_tuple}')
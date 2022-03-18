from builtins import print

my_list = [1, 'jhf', 'jhfjhgfjh', 5, 8957, 456.2]

sum_element = ''
for element in my_list:
    if not type(element) == 'str':
        element = str(element)
        sum_element = f"sum_element - {sum_element + '---' + element}"

my_new_list = sum_element.split()

my_new_list2 = []

for new_element in my_new_list:
    if new_element != '-':
        my_new_list2.append(new_element)

print(f"New {my_new_list2}")

i = len(my_new_list2)
while i >= 0:
    i -= 1
    if my_new_list2[i] == 'sum_element':
        print(f" {i} + {my_new_list2[i]}")
        del my_new_list2[i]
    else:
        print(f" +++ {my_new_list2[i]}")
print(f" UUU------- {my_new_list2}")

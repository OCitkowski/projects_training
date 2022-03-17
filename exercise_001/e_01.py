from builtins import print

my_list = [1, 'jhf', 'jhfjhgfjh', 5, 8957, 456.2]
#print(my_list)
#print('start')
sum_element = ''
for element in my_list:
    #print(element)
    if not type(element) == 'str':
        element = str(element)
        sum_element = f"sum_element - {sum_element + '---' + element}"
        # print(sum_element)

# count_sum_element = sum_element.count()
# print(count_sum_element)
#print(f" {sum_element} --- {type(sum_element)}")
my_new_list = sum_element.split()
#print(my_new_list)

my_new_list2 = []
for new_element in my_new_list:
    if not new_element == '-':
        my_new_list2.append(new_element)

print(f"New {my_new_list2}")

for new_element2 in my_new_list2:
    if new_element2 == 'sum_element':
        print(f" {my_new_list2} + {new_element2}")
        my_new_list2.remove('sum_element')
    else:
        print(f" +++ {new_element2}")
print(f" UUU------- {my_new_list2}")

import test_module
from test_module import build_profile as my_build_profile
# *****************************8.3**********************

print(test_module.make_pizza(2343, 'in city'))

user_profile = my_build_profile('sani', 'ci', location = 'in city', phone = '454343545')
print(user_profile)


# def city_country(contry, city):
#     return f'{contry}, {city}'
# city_country_formated = city_country('Ukraine', 'Kyiv')
# print(city_country_formated)
#
# def make_album(first_name, last_name, middle_name, age, id = None):
#
#     if id:
#         my_list = [first_name, last_name, middle_name, age, id ]
#     else:
#         my_list = [first_name, last_name, middle_name, age, "not have id"]
#     my_dictionary = {}
#     my_dictionary[first_name] = my_list
#
#     return my_dictionary
#
# formated_album = make_album('alex', 'ci', 'volod', '43')
# print(formated_album)
#
# formated_album = make_album('alex', 'ci', 'volod', '43', 76654654564)
# print(formated_album)
# # **************************************8.2
# def get_input_list(phone_list=None):
#
#     if not phone_list:
#         phone_list = []
#     active = True
#
#     while active:
#         first_name = input('enter first name -\n')
#         if not first_name:
#             continue
#         elif first_name =='exit':
#             break
#
#         last_name = input('enter last name - \n')
#         if not last_name:
#             continue
#         elif last_name == 'exit':
#             break
#
#         phone = input('enter your phone number - \n')
#         if not phone:
#             continue
#         elif phone == 'exit':
#             break
#
#         tin = input('enter your TIN code - \n')
#         if not tin:
#             continue
#         elif tin == 'exit':
#             break
#
#         phone_list.append({phone: [first_name, last_name, tin]})
#
#     return phone_list
#
# main_phone_list = [{'34565656': ['afgfdg', 'dfghfdgh', '456546']}, {'45656': ['dsftghgfh', 'fhgh', '4565']}]
# main_phone_list2 = get_input_list(main_phone_list[:])
#
# for item in main_phone_list:
#     print(item)









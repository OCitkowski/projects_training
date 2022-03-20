
def city_country(contry, city):
    return f'{contry}, {city}'
city_country_formated = city_country('Ukraine', 'Kyiv')
print(city_country_formated)

def make_album(first_name, last_name, middle_name, age, id = None):

    if id:
        my_list = [first_name, last_name, middle_name, age, id ]
    else:
        my_list = [first_name, last_name, middle_name, age, "not have id"]
    my_dictionary = {}
    my_dictionary[first_name] = my_list

    return my_dictionary

formated_album = make_album('alex', 'ci', 'volod', '43')
print(formated_album)

formated_album = make_album('alex', 'ci', 'volod', '43', 76654654564)
print(formated_album)



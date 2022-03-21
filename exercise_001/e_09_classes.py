from car_test import ElectroCar
from car_test import Car

my_car = Car("opel", "corsa", 2017)
my_car.read_odometr()
my_car.increment_odometr(45)
my_car.read_odometr()


my_tesla = ElectroCar("tesla", "model s", 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# ************************9.1*******
# class Dog:
#     """Dog, is my dog"""
#
#     def __init__(self, name, age):
#         """initialise name and atribute of dog"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """simuliate command sit"""
#
#         print(f' sit {self.name}')
#
#     def roll_over(self):
#         """simuliate command roll"""
#
#         print(f' roll {self.name}')
#
# my_dog_1 = Dog("Fufu", 16)
# print(f'NAME - {my_dog_1.name}; AGE - {my_dog_1.age} ')
# my_dog_1.sit()
# my_dog_1.roll_over()
#
# my_dog_2 = Dog("Putiy", 24)
# print(f' the second dog named {my_dog_2.name} and it have {my_dog_2.age} year old')




# ********************9.2***********
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def get_desccriptive_name(self):
        """return formated name"""
        long_name = f'{self.make} {self.year} {self.model}'
        return long_name
    def read_odometr(self):
        """prin odometr value"""
        print(f'this car has - {self.odometr}  km')
    def update_odometr(self, milwage):
        """set odometr value for car"""
        if self.odometr <= milwage:
            self.odometr = milwage
        else:
            print(f"dont touch")
    def increment_odometr(self, miles):
        """Add km to auto miles"""
        self.odometr += miles


my_new_car = Car("opel", "a4", 2022)
my_new_car.odometr = 89
print(my_new_car.get_desccriptive_name().title())
my_new_car.read_odometr()
my_new_car.update_odometr(5)
my_new_car.read_odometr()
my_new_car.increment_odometr(54)
my_new_car.read_odometr()

# ************************9.1*******
class Dog:
    """Dog, is my dog"""

    def __init__(self, name, age):
        """initialise name and atеribute of dog"""
        self.name = name
        self.age = age

    def sit(self):
        """simuliate command sit"""

        print(f' sit {self.name}')

    def roll_over(self):
        """simuliate command roll"""

        print(f' roll {self.name}')

my_dog_1 = Dog("Fufu", 16)
print(f'NAME - {my_dog_1.name}; AGE - {my_dog_1.age} ')
my_dog_1.sit()
my_dog_1.roll_over()

my_dog_2 = Dog("Putiy", 24)
print(f' the second dog named {my_dog_2.name} and it have {my_dog_2.age} year old')





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




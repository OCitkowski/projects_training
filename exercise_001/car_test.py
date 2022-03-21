# ********************9.2***********
class Battery:
    """modeling battery for car"""
    def __init__(self, battery_size=75):
        """initialize battey of car"""
        self.battery_size = battery_size

    def describe_battery(self):
        """output data"""
        print(f"this car has a {self.battery_size} -kWh battery")

    def get_range(self):
        range_battery = self.battery_size * 100
        print(f" This car can go about {range_battery} miles on fuul charge")


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

    def fill_gas_tank(self):
        print(f"fill gas tank for this car is ok.")


class ElectroCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

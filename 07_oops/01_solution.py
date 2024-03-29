class Car:
    #class variable
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # self.total_car += 1
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    @property
    def get_model(self):
        return self.__model

    def full_name(self):
        return f"Brand:{self.__brand}, Model:{self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.model)
# # print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.full_name())

# print(my_tesla.fuel_type())
# safari = Car("Tata", "Safari")
# safari.model = "City"
# print(safari.get_model)
# safari.get_model = "City" # not possible

# print(safari.model)
# print(safari.get_model())
# print(safari.model)
# print(Car.general_description())
# print(safari.general_description()) 

# print(safari.fuel_type())

# print(safari.total_car)

# test = Car("test", "test")
# print(test.total_car)

# print(Car.total_car)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand, my_car.model)

# print(my_car.full_name())

# my_tata = Car("Tata", "Safari")
# print(my_tata.brand, my_tata.model)

# print(my_tata.full_name())

class Battery:
    def batter_info(self):
        return 'this is battery'

class Engine:
    def engine_info(self):
        return 'this is engine'

class ElectricCarTwo(Battery, Engine, Car):
    pass

new_tesla = ElectricCarTwo("Tesla", "Model S")
print(new_tesla.batter_info())
print(new_tesla.engine_info())
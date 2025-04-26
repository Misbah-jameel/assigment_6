class Car:
    def __init__(self,brand):
        self.brand = brand 

    def start(self):  # public method
        print(self.brand, "car started!")

my_car = Car("Toyota")

print("Brand:", my_car.brand)

my_car.start()
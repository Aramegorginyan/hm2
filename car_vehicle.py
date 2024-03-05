class Vehicle:
    vehicle_count = 0

    def __init__(self,make,model):
        self.make = make
        self.model = model
        Vehicle.vehicle_count += 1

    def increment_vehicle_count(self):
        self.vehicle_count += 1

    def start_engine(self):
        print("Engine started")

    def __repr__(self):
        return(f"{self.make},{self.model}")

class ElectricVehicle:
    def __init__(self,battery_capacity):
        self.battery_capacity = battery_capacity

class Car(Vehicle):
    def __init__(self,make,model,number_of_wheels=4):
        super().__init__(make,model)
        self.number_of_wheels = number_of_wheels

    def start_engine(self):
        print("Car engine started")
        super().start_engine()

    def get_vehicle_count(cls):
        return cls.vehicle_count

    def __repr__(self):
        return(f"{super().__repr__()},{self.number_of_wheels}")

class ElectricCar(Car,ElectricVehicle):
    def __init__(self, make, model, number_of_wheels=4, battery_capacity=0):
        Car.__init__(self,make,model,number_of_wheels=4)
        ElectricVehicle.__init__(self, battery_capacity)

    def __repr__(self):
        return(f"{super().__repr__()},{self.battery_capacity}")

c = Car("Toyota", "Camry",42)
c.start_engine()

e_car = ElectricCar("Tesla","CuberTruck",battery_capacity=1300)
print(ElectricCar.__mro__)
# Creating a class for vehicles for a polymorphism example

class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"
    
class Boat:
    def move(self):
        return "Sailing"

class Spaceship:
    def move(self):
        return "Launching"

# Creating objects for the vehicles
car = Car()
plane = Plane()
boat = Boat()
spaceship = Spaceship()

# Using the methods for the vehicles
print(car.move())
print(plane.move())
print(boat.move())
print(spaceship.move())


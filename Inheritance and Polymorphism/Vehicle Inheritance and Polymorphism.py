class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

# Create instances of each class
car1 = Car("Ford", "Mustang")        # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")      # Create a Plane object

# Iterate over the objects
for x in (car1, boat1, plane1):
    print(f"Brand: {x.brand}, Model: {x.model}")
    x.move()
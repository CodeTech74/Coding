class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

    def space(self):
        return f"The {self.name} contain more people than a regular car"
    
School_bus = Bus("School Volvo", 180, 120)
print(f"Vehicle Name: {School_bus.name}\nSpeed: {School_bus.max_speed}km/h\nMileage: {School_bus.mileage}km")
print(School_bus.space())
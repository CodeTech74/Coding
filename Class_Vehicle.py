class Vehicle:
    def __init__(self, max_speed, mileage, color):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

Daddy_car = Vehicle(240, 18, "Blue")      
Mummy_car = Vehicle(220, 38, "Black")   

print("Daddy's Car Max Speed:",Daddy_car.max_speed)
print("Daddy's Car Mileage:", Daddy_car.mileage)
print("Daddy's Car Color:", Daddy_car.color)
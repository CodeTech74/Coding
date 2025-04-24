class BMW:
    """
    Represents a BMW car.
    """

    def __init__(self, model, color, year):
        """
        Initializes a BMW object.

        Parameters:
            model (str): The model of the BMW.
            color (str): The color of the BMW.
            year (int): The manufacturing year of the BMW.
        """
        self.model = model
        self.color = color
        self.year = year

    def start(self):
        """
        Simulates starting the BMW engine.
        """
        print(f"BMW {self.model} is starting its engine.")

    def accelerate(self):
        """
        Simulates accelerating the BMW.
        """
        print(f"BMW {self.model} is accelerating.")

    def brake(self):
        """
        Simulates braking the BMW.
        """
        print(f"BMW {self.model} is braking.")

    def display_info(self):
        """
        Displays information about the BMW.
        """
        print(f"BMW {self.model} - Color: {self.color}, Year: {self.year}")



class Ferrari:
    """
    Represents a Ferrari car.
    """

    def __init__(self, model, color, year):
        """
        Initializes a Ferrari object.

        Parameters:
            model (str): The model of the Ferrari.
            color (str): The color of the Ferrari.
            year (int): The manufacturing year of the Ferrari.
        """
        self.model = model
        self.color = color
        self.year = year

    def start(self):
        """
        Simulates starting the Ferrari engine.
        """
        print(f"Ferrari {self.model} is roaring to life!")

    def accelerate(self):
        """
        Simulates accelerating the Ferrari.
        """
        print(f"Ferrari {self.model} is speeding off!")

    def brake(self):
        """
        Simulates braking the Ferrari.
        """
        print(f"Ferrari {self.model} is screeching to a halt!")

    def display_info(self):
        """
        Displays information about the Ferrari.
        """
        print(f"Ferrari {self.model} - Color: {self.color}, Year: {self.year}")



# Polymorphism in action
def car_actions(car):
    """
    Performs actions on any car object (BMW or Ferrari).  This function
    demonstrates polymorphism.  It doesn't care about the specific type of
    car; it just calls the methods defined in the common interface.

    Parameters:
        car (BMW or Ferrari): An object of either the BMW or Ferrari class.
    """
    car.display_info() # Calls the display_info method of the car object
    car.start()  # Calls the start method of the car object
    car.accelerate()  # Calls the accelerate method of the car object
    car.brake()  # Calls the brake method of the car object
    print("-" * 30) # Separator for better output

# Example Usage
if __name__ == "__main__":
    # Create instances of BMW and Ferrari
    bmw = BMW("X5", "Blue", 2023)
    ferrari = Ferrari("F8 Tributo", "Red", 2022)

    # Demonstrate polymorphism by calling car_actions with different car objects
    car_actions(bmw)
    car_actions(ferrari)

    # Example of using a list of cars
    cars = [bmw, ferrari]
    for car in cars:
        car_actions(car)

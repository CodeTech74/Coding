class Vehicle:
    """
    This class represents a generic vehicle.

    Attributes:
        name (str): The name of the vehicle.
        max_speed (int): The maximum speed of the vehicle.
        mileage (int): The mileage of the vehicle.
    """

    def __init__(self, name, max_speed, mileage):
        """
        Initializes a Vehicle object with name, max_speed, and mileage.

        Parameters:
            name (str): The name of the vehicle.
            max_speed (int): The maximum speed of the vehicle.
            mileage (int): The mileage of the vehicle.
        """
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        """
        Returns a string representation of the Vehicle object.

        Returns:
            str: A string describing the vehicle's attributes.
        """
        return f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"

    def seating_capacity(self, capacity):
        """
        Returns a string describing the seating capacity of the vehicle.

        Parameters:
            capacity (int): The seating capacity.

        Returns:
            str: String indicating the seating capacity.
        """
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    """
    This class represents a bus, inheriting from the Vehicle class.
    It adds a method to calculate the total fare.
    """

    def __init__(self, name, max_speed, mileage):
        """
        Initializes a Bus object with name, max_speed, and mileage.
        Calls the constructor of the parent class (Vehicle).

        Parameters:
            name (str): The name of the bus.
            max_speed (int): The maximum speed of the bus.
            mileage (int): The mileage of the bus.
        """
        super().__init__(name, max_speed, mileage)  # Call parent class constructor

    def seating_capacity(self, capacity=50):
        """
        Calculates the seating capacity of the bus.  Overrides the
        seating_capacity method in the Vehicle class.  Provides a default
        capacity of 50.

        Parameters:
            capacity (int, optional): The seating capacity of the bus.
                Defaults to 50.

        Returns:
            str: String indicating the seating capacity.
        """
        return super().seating_capacity(capacity) # Call parent class method

    def fare(self):
        """
        Calculates the total fare for the bus, based on a base fare and mileage.

        Returns:
            int: The total fare for the bus.
        """
        base_fare = 100  # Base fare for the bus
        total_fare = base_fare + (self.mileage * 0.10)  # 10% of mileage
        return total_fare

# Example Usage
if __name__ == "__main__":
    # Create a Bus object
    school_bus = Bus("School Bus", 120, 10)

    # Print the bus object
    print(school_bus)

    # Print the seating capacity of the bus
    print(school_bus.seating_capacity())  # Uses the default capacity

    # Calculate and print the fare for the bus
    print(f"Total fare is: {school_bus.fare()}")

    # Example of calling the Vehicle class's seating_capacity method.
    vehicle1 = Vehicle("Generic Vehicle", 100, 20)
    print(vehicle1.seating_capacity(30))

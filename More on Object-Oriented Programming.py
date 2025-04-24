import math

class Circle:
    """
    This class represents a circle with a given radius.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle object with the given radius.

        Parameters:
            radius (float): The radius of the circle.  Must be non-negative.
        Raises:
            ValueError: If the radius is negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def __str__(self):
        """
        Returns a string representation of the Circle object.

        Returns:
            str: A string describing the circle's radius.
        """
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        """
        Official string representation for developers (useful for debugging).
        Returns:
            str:  A string that can be used to recreate the object.
        """
        return f"Circle({self.radius})"
# Example Usage
if __name__ == "__main__":
    try:
        # Create a Circle object with radius 5.
        circle1 = Circle(5)
        print(circle1)  # Uses the __str__ method

        # Calculate and print the area.
        area1 = circle1.area()
        print(f"Area of circle1: {area1:.2f}")

        # Calculate and print the perimeter.
        perimeter1 = circle1.perimeter()
        print(f"Perimeter of circle1: {perimeter1:.2f}")

        # Create another circle with radius 10.
        circle2 = Circle(10)
        print(circle2)

        area2 = circle2.area()
        print(f"Area of circle2: {area2:.2f}")
        perimeter2 = circle2.perimeter()
        print(f"Perimeter of circle2: {perimeter2:.2f}")

        # Example of handling a negative radius (will raise ValueError)
        # circle3 = Circle(-3)
    except ValueError as e:
        print(f"Error: {e}")
    
    #Demonstrate the use of the __repr__ method
    circle3 = Circle(7)
    print(repr(circle3)) # Output: Circle(7)
    

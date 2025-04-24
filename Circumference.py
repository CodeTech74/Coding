import math

def calculate_circumference(radius):
    """
    Calculates the circumference of a circle.

    Args:
        radius: The radius of the circle (numeric value).

    Returns:
        The circumference of the circle (float).
        Returns None if the radius is not a valid number.
    """
    if not isinstance(radius, (int, float)):
        return None # Return None for invalid input

    if radius < 0:
        return None #Return None for negative input

    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
radius1 = 5
circumference1 = calculate_circumference(radius1)
if circumference1 is not None:
    print(f"The circumference of a circle with radius {radius1} is: {circumference1}")
else:
    print("Invalid radius input.")

radius2 = 0
circumference2 = calculate_circumference(radius2)
if circumference2 is not None:
    print(f"The circumference of a circle with radius {radius2} is: {circumference2}")
else:
    print("Invalid radius input.")

radius3 = -2
circumference3 = calculate_circumference(radius3)
if circumference3 is not None:
    print(f"The circumference of a circle with radius {radius3} is: {circumference3}")
else:
    print("Invalid radius input.")

radius4 = "abc"
circumference4 = calculate_circumference(radius4)
if circumference4 is not None:
    print(f"The circumference of a circle with radius {radius4} is: {circumference4}")
else:
    print("Invalid radius input.")
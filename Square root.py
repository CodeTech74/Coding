import math

# Input from the user
number = input("Enter a number to calculate its square root: ")

try:
    # Convert the input to a float
    number = float(number)
    
    if number < 0:
        print("Square root of a negative number is not real.")
    else:
        # Calculate the square root
        square_root = math.sqrt(number)
        print(f"The square root of {number} is: {square_root}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

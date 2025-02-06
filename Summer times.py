# Program to check if a number is positive, negative, or zero

# Input from the user
number = input("Enter a number: ")

try:
    # Convert the input to a float
    number = float(number)
    
    # Conditional statements
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number is zero.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

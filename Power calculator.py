# Program to calculate the n-th power of a given number

# Input from the user
base = input("Enter the base number: ")
exponent = input("Enter the exponent (power): ")

try:
    # Convert inputs to floats for general use
    base = float(base)
    exponent = float(exponent)
    
    # Calculate the power
    result = base ** exponent
    print(f"The result of {base} raised to the power {exponent} is: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")

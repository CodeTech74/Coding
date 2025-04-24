def get_valid_age():
    """
    Prompts the user to enter their age and validates the input.
    Returns the age as an integer if valid, or None if invalid.
    """
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative.")
            elif age > 150:  # Reasonable upper limit for human age
                print("Please enter a realistic age.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_even_odd(age):
    """
    Checks if the given age is even or odd and prints the result.
    """
    if age % 2 == 0:
        print(f"Your age ({age}) is even.")
    else:
        print(f"Your age ({age}) is odd.")

# Main program
age = get_valid_age()

if age is not None:
    check_even_odd(age)
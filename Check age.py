# Program to check if the age is between 10 and 20 years

# Input from the user
age = input("Enter your age: ")

try:
    # Convert the input to an integer
    age = int(age)
    
    # Check if the age is between 10 and 20
    if 10 <= age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is NOT between 10 and 20 years.")
except ValueError:
    print("Invalid input. Please enter a numeric value for age.")

# Program to calculate the total number of digits in a number

# Input from the user
number = input("Enter a number: ")

# Convert the input to an absolute integer to handle negative numbers
try:
    number = abs(int(number))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Initialize the digit count
digit_count = 0

# Use a while loop to count digits
while number > 0:
    number //= 10  # Remove the last digit
    digit_count += 1

# Output the result
print(f"The total number of digits is: {digit_count}")

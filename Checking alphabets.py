# Program to check if a given character is an alphabet

# Input from the user
char = input("Enter a character: ")

# Check if the input has exactly one character
if len(char) != 1:
    print("Please enter a single character.")
else:
    # Check if the character is an alphabet
    if char.isalpha():
        print(f"The character '{char}' is an alphabet.")
    else:
        print(f"The character '{char}' is not an alphabet.")

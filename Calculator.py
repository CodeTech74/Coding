def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    """Simple command-line calculator."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True: #Loop to allow for multiple calculations.
        try:
            choice = input("Enter choice (1/2/3/4): ")

            if choice not in ('1', '2', '3', '4'):
                print("Invalid input")
                continue #restart the loop.

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                break #exit the loop
        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    calculator()
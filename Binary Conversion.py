def decimal_to_binary(decimal_num):
    """
    Converts a decimal number to its binary representation.

    Args:
        decimal_num: The decimal number to convert (integer).

    Returns:
        The binary representation of the decimal number (string).
        Returns None if the input is not an integer.
    """
    if not isinstance(decimal_num, int):
        return None

    if decimal_num == 0:
        return "0"

    binary = ""
    num = abs(decimal_num) #handle negative numbers by converting to positive and then adding a negative sign at the end if needed.
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    if decimal_num < 0:
      binary = "-" + binary

    return binary

# Example usage:
decimal1 = 10
binary1 = decimal_to_binary(decimal1)
if binary1 is not None:
    print(f"Binary of {decimal1} is: {binary1}")
else:
    print("Invalid input.")

decimal2 = 25
binary2 = decimal_to_binary(decimal2)
if binary2 is not None:
    print(f"Binary of {decimal2} is: {binary2}")
else:
    print("Invalid input.")

decimal3 = 0
binary3 = decimal_to_binary(decimal3)
if binary3 is not None:
    print(f"Binary of {decimal3} is: {binary3}")
else:
    print("Invalid input.")

decimal4 = -10
binary4 = decimal_to_binary(decimal4)
if binary4 is not None:
    print(f"Binary of {decimal4} is: {binary4}")
else:
    print("Invalid input.")

decimal5 = "abc"
binary5 = decimal_to_binary(decimal5)
if binary5 is not None:
    print(f"Binary of {decimal5} is: {binary5}")
else:
    print("Invalid input.")
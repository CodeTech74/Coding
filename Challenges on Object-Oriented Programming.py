class IntToRomanConverter:
    """
    This class converts integer values to Roman numerals.
    """

    def __init__(self):
        """
        Initializes the IntToRomanConverter with the Roman numeral lookup table.
        """
        self.roman_map = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        self.values = sorted(self.roman_map.keys(), reverse=True) # Store values for efficiency

    def convert(self, num):
        """
        Converts an integer to its Roman numeral representation.

        Args:
            num (int): The integer to convert.

        Returns:
            str: The Roman numeral representation of the integer.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input integer is not within the valid range (1 to 3999).
        """
        if not isinstance(num, int):
            raise TypeError("Input must be an integer.")
        if not 1 <= num <= 3999:
            raise ValueError("Input must be between 1 and 3999 (inclusive).")

        roman_numeral = ''
        for value in self.values:
            while num >= value:
                roman_numeral += self.roman_map[value]
                num -= value
        return roman_numeral

# Example Usage
if __name__ == "__main__":
    # Create an instance of the IntToRomanConverter class
    converter = IntToRomanConverter()

    # Test cases
    test_numbers = [1, 4, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000, 1994, 3999, 245]
    for number in test_numbers:
        roman_numeral = converter.convert(number)
        print(f"{number} in Roman numerals is: {roman_numeral}")

    # Error handling examples
    try:
        print(converter.convert(0))  # Value out of range
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print(converter.convert(4000))  # Value out of range
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print(converter.convert("abc"))  # Invalid input type
    except TypeError as e:
        print(f"Error: {e}")
    
    try:
        print(converter.convert(3.14)) # Invalid input type
    except TypeError as e:
        print(f"Error: {e}")

class StringReverser:
    """
    This class provides a method to reverse the words in a given string.
    """

    def reverse_words(self, input_string):
        """
        Reverses the order of words in the input string.

        Args:
            input_string (str): The string to be reversed.

        Returns:
            str: The string with the words reversed.  Returns an empty string
                 if the input is None or empty.
        """
        if not input_string:  # Handle None or empty string
            return ""

        words = input_string.split()  # Split the string into a list of words
        reversed_words = words[::-1]  # Reverse the list of words
        return " ".join(reversed_words)  # Join the reversed words back into a string

# Example Usage
if __name__ == "__main__":
    # Create an instance of the StringReverser class
    string_reverser = StringReverser()

    # Test case 1:  A normal sentence
    test_string1 = "hello world"
    reversed_string1 = string_reverser.reverse_words(test_string1)
    print(f"Original string: '{test_string1}'")
    print(f"Reversed string: '{reversed_string1}'")  # Output: 'world hello'

    # Test case 2:  A sentence with leading/trailing spaces
    test_string2 = "  the sky is blue  "
    reversed_string2 = string_reverser.reverse_words(test_string2)
    print(f"Original string: '{test_string2}'")
    print(f"Reversed string: '{reversed_string2}'")  # Output: 'blue is sky the'

    # Test case 3:  A sentence with multiple spaces between words
    test_string3 = "one    two three"
    reversed_string3 = string_reverser.reverse_words(test_string3)
    print(f"Original string: '{test_string3}'")
    print(f"Reversed string: '{reversed_string3}'")  # Output: 'three two one'

    # Test case 4:  An empty string
    test_string4 = ""
    reversed_string4 = string_reverser.reverse_words(test_string4)
    print(f"Original string: '{test_string4}'")
    print(f"Reversed string: '{reversed_string4}'")  # Output: ''

    # Test case 5: A None input
    test_string5 = None
    reversed_string5 = string_reverser.reverse_words(test_string5)
    print(f"Original string: '{test_string5}'")
    print(f"Reversed string: '{reversed_string5}'") # Output: ''

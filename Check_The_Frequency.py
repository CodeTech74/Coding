def check_frequency(test_dict, value_to_check):
  """
  Checks the frequency of a value in a dictionary.

  Args:
    test_dict: The dictionary to check.
    value_to_check: The value to find the frequency of.

  Returns:
    The frequency (count) of the value in the dictionary's values.
  """
  count = 0
  for value in test_dict.values():
    if value == value_to_check:
      count += 1
  return count

# Example Usage:
test_dictionary = {'a': 5, 'b': 10, 'c': 5, 'd': 15, 'e': 5}
value = 5
frequency = check_frequency(test_dictionary, value)
print(f"The frequency of {value} in the dictionary is: {frequency}")

value2 = 10
frequency2 = check_frequency(test_dictionary, value2)
print(f"The frequency of {value2} in the dictionary is: {frequency2}")

value3 = 20
frequency3 = check_frequency(test_dictionary, value3)
print(f"The frequency of {value3} in the dictionary is: {frequency3}")

empty_dictionary = {}
frequency_empty = check_frequency(empty_dictionary, 5)
print(f"The frequency of 5 in the empty dictionary is: {frequency_empty}")
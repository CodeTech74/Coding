# Program demonstrating string operations

# Input a string from the user
user_string = input("Enter a string: ")

# String operations
# 1. Length of the string
length = len(user_string)
print(f"The length of the string is: {length}")

# 2. Convert to uppercase
uppercase = user_string.upper()
print(f"The string in uppercase is: {uppercase}")

# 3. Convert to lowercase
lowercase = user_string.lower()
print(f"The string in lowercase is: {lowercase}")

# 4. Count occurrences of a specific character
char_to_count = input("Enter a character to count its occurrences: ")
count = user_string.count(char_to_count)
print(f"The character '{char_to_count}' appears {count} time(s).")

# 5. Check if the string starts with a specific substring
start_substring = input("Enter a substring to check if the string starts with it: ")
starts_with = user_string.startswith(start_substring)
print(f"Does the string start with '{start_substring}'? {starts_with}")

# 6. Check if the string ends with a specific substring
end_substring = input("Enter a substring to check if the string ends with it: ")
ends_with = user_string.endswith(end_substring)
print(f"Does the string end with '{end_substring}'? {ends_with}")

# 7. Replace a substring with another
to_replace = input("Enter a substring to replace: ")
replacement = input(f"Enter the new substring to replace '{to_replace}' with: ")
replaced_string = user_string.replace(to_replace, replacement)
print(f"The updated string is: {replaced_string}")

# 8. Reverse the string
reversed_string = user_string[::-1]
print(f"The reversed string is: {reversed_string}")

# 9. Check if the string is a palindrome
is_palindrome = user_string == reversed_string
print(f"Is the string a palindrome? {is_palindrome}")

# 10. Split the string into words
words = user_string.split()
print(f"The string split into words: {words}")

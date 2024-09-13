def is_palindrome(string):
  """Checks if a string is a palindrome."""
  string = string.lower()  # Convert to lowercase to ignore case
  return string == string[::-1]

# Get input from the user
string = input("Enter a string: ")

# Check if it's a palindrome
if is_palindrome(string):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")
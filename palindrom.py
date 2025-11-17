def is_palindrome(s):
    """Check if the input string s is a palindrome."""
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_s == cleaned_s[::-1]

input_string = input("Enter a string to check for palindrome: ")
if is_palindrome(input_string):
    print(f'True: "{input_string}" is a palindrome.') 
else:
    print(f'False: "{input_string}" is not a palindrome.')     
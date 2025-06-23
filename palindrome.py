str = input("Enter a number?")

re = str[::-1]
if re == str:
    print("Palindrome")
else:
    print("Not a palindrome")
# #............................
# def is_palindrome(s: str) -> bool:
#     # Convert to lowercase and remove non-alphanumeric characters
#     s = ''.join(char.lower() for char in s if char.isalnum())
    
#     # Two-pointer technique
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# # Test the function
# test_string = "A man, a plan, a canal: Panama"
# print(f"Is the string '{test_string}' a palindrome? {is_palindrome(test_string)}")

# q1. Count the number of vowels and consonants in a string.

# input = input("Enter a string : ").lower()

# vowels = "aeiou"
# vowelCount = 0
# constCount = 0

# for char in input:
#     if char.isalpha(): #isaplha doesnt count spaces and special chars as consonanats
#         if char in vowels :
#             vowelCount += 1
#         else:
#             constCount += 1

# print(f"There were {vowelCount} vowels and {constCount} constants")

# -----------------------------------------------------------------------------------------

# q2. Reverse a string without using slicing.

# str = input("Enter a string : ")
# rev = ""

# for ch in str:
#     rev = ch + rev

# print(f"Reverse of {str} is {rev}")

# ----------------------------------------------------------------------------------------------------

# # q3. Check whether a string is a palindrom. 

# str = input("Enter a string : ")
# rev = ""

# for ch in str:
#     rev = ch + rev

# if str == rev:
#     print(f"{str} is a palindrome")
# else:
#     print("Not a palindrome")

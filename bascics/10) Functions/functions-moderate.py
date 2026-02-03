# q1. Write a function that takes a list of numbers and returns the maximum value (do NOT use max()).

# def findMax(numbers):
#     maxVal = numbers[0]
#     for n in numbers:
#         if n > maxVal:
#             maxVal = n
#     return print(maxVal)

# findMax([1, 2, 3, 4])

# --------------------------------------------------------------------------------------------

# q2. Write a function that counts how many times a given character appears in a string.

# def charCounter(text, char):
#     charCount = 0
#     for i in text:
#         if i == char:
#             charCount += 1
#     return print(charCount)

# charCounter("afeef", "e")

# -----------------------------------------------------------------------------

# q3. Write a function that returns the factorial of a number using a loop.

# def factCounter(num):
#     fact = 1
#     for i in range(num, 0, -1):
#         fact *= i
#     return fact

# print(factCounter(3))
# q1. Write a function that takes a list of integers and returns a new list containing only unique values, preserving order (do NOT use set()).

# def uniqueVals(numbers):
#     uniqueList = []
#     for num in numbers:
#         if num not in uniqueList:
#             uniqueList.append(num)
#     return uniqueList

# print(uniqueVals([1, 2, 2, 3, 4, 5, 6, 5, 5]))

# --------------------------------------------------------------------------------

# q2. Write a function that accepts a sentence and returns a dictionary with word counts.

# def wordCount(sentence):
#     words = sentence.split()
#     result = {}

#     for word in words:
#         if word in result:
#             result[word] += 1
#         else:
#             result[word] = 1

#     return result

# print(wordCount("git gitHub figma git"))


# --------------------------------------------------------------------------------------

# q3. Write a function that validates a password with these rules:

    # At least 8 characters

    # Contains at least one digit

    # Contains at least one uppercase letter

    # Return True or False.

# def passchecker(password):
#     hasDigit = False
#     hasUpper = False

#     if len(password) < 8:
#         return False
    
#     for i in password:
#         if i.isdigit():
#             hasDigit = True
#         if i.isupper():
#             hasUpper = True

#     return hasDigit and hasUpper

# print(passchecker("afeefA123"))
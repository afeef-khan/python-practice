# q1. Given a list of words, create a dictionary that stores each word and its length.

# words = ["Afeef", "Tadeeb", "Hassaan"]
# dict = {}

# for i in words:
#     dict[i] = len(i)

# print(dict)

# --------------------------------------------------------------------------------------------

# q2. Write a program to merge two dictionaries. If a key exists in both, add their values.

# d1 = {"a" : 1, "b" : 2, "c" : 3}
# d2 = {"c" : 3, "d" : 4, "e" : 5}

# result = d1.copy()

# for key, value in d2.items():
#     if key in result:
#         result[key] += value
#     else:
#         result[key] = value

# print(result)

# -------------------------------------------------------------------------------

# q3. Count the frequency of each character in a string using a dictionary.

# my approach
# str = "hassaan"
# freq = {}

# for char in str:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# print(freq)

# real answer
# text = "programming"
# freq = {}

# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1

# print(freq)

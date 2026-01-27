# q1. Write a program to swap two variables using a tuple, without a temporary variable.

# a = (1)
# b = (2)

# a, b = b, a
# print(a, b)

# --------------------------------------------------------
# q2. Find the maximum and minimum element in a tuple without using built-in functions.

# t = (1, 2, 3, 4)

# max = t[0]
# min = t[0]

# for i in t:
#     if i > max:
#         max = i
#     if i < min:
#         min = i

# print(f"{max} is the largest number and {min} is the smallest")

# ----------------------------------------------------------------------------------

# q3. Given a tuple of tuples, extract only the second element from each inner tuple.

# t = ((1, 2), (3, 4), (5, 6))
# result = []

# for i in t:
#     result.append(i[1])

# print(result) 
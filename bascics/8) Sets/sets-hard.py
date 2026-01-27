# q1. Check if two lists contain exactly the same unique elements.

# l1 = [1, 2, 3]
# l2 = [3, 2, 5]

# if set(l1) == set(l2):
#     print("both lists are same")
# else:
#     print("lists are different")

# -------------------------------------------------------------

# q2. Find elements that appear in exactly one of two sets.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# result = set1 ^ set2
# print(result)

# --------------------------------------------------------------------

# q3. Count how many unique numbers appear more than once in a list.

# l = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7]

# seen = set()
# duplicate = set()

# for n in l:
#     if n in seen:
#         duplicate.add(n)
#     else:
#         seen.add(n)

# print(f"Total duplicates = {len(duplicate)}")
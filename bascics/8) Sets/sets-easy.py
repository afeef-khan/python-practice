# q1. Create a set from a list and remove duplicate values.

# l = [1, 2, 3, 1, 4, 5]
# s = set(l)

# print(s)

# ------------------------------------------------------------------------

# q2. Add an element to a set and remove another element safely.

# s = {1, 2, 3}

# s.add(5)
# s.discard(2)

# print(s)

# ------------------------------------------------------------------------

# q3. Check whether a given element exists in a set.

s = {1, 2, 3, 4, 5}
num = 2

if num in s:
    print(f"{num} is in set")
else:
    print(f"{num} not in set!")
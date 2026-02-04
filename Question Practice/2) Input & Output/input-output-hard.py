# q1. Take an unknown number of integers in one line and print their maximum.

# input = input("Enter numbers seperated by a string : ").split()
# input always returns a string so, The method here cuts string on spaces and gives us a list of string

# input = [int(n) for n in input]
# converts list of string in list of int

# print("Maximum number is :",  max(input))
# max() is a built in python function

# -----------------------------------------------------------------------------------------

# q2. Take a sentence as input and print the number of words.

# this approach manages the spaces by using split() method
    # input = input("Enter some words : ").strip()
    # words = input.split()
    # print("Words Count :", len(words))

#-----------------------------------------------------------------------------------------

# q3. Take input for principal, rate, and time, then print simple interest rounded to 2 decimal places.

# principal = float(input("Principal = "))
# rate = float(input("Rate = "))
# time = float(input("Time = "))

# interest = (principal * rate * time) / 100

# print(f"Simple Interest = {interest:.2f}")
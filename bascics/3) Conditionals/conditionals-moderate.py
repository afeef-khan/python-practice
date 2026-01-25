# q1. Write a program to find the largest of three numbers.

# a = int(input("Enter Ist number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))

# if a >= b and a >= c:
#     print("Ist number is largest")
# elif b >= a and b >= c:
#     print("2nd number is largest")
# else:
#     print("3rd number is largest")

# -----------------------------------------------------------------------------

# q2. Write a program to calculate electricity bill:
# Units ≤ 100 → ₹2/unit
# Units 101–200 → ₹3/unit
# Units > 200 → ₹5/unit

# My normal version
# units = int(input("Enter units consumed : "))

# if units <= 100:
#     print(f"Units of ₹{2 * units} were consumed!")
# elif units < 200:
#     print(f"Units of ₹{3 * units} were consumed!")
# elif units >= 200:
#     print(f"Units of ₹{5 * units} were consumed!")

# # Enchanced version
# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = units * 3
# else:
#     bill = units * 5

# print("Electricity Bill: ₹", bill)

# ------------------------------------------------------------------------------------

# q3. Write a program to check if a year is a leap year.

# year = int(input("Enter the year : "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Its a leap year!")
# else:
#     print("Its not a leap year!")
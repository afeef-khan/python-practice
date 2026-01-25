# q1. Reverse a number using a loop (without converting to string).

# num = int(input("Enter a number : "))
# revNum = 0

# while num > 0:
#     digit = num % 10
#     revNum = revNum * 10 + digit
#     num //= 10

# print("Reversed num =", revNum)

# ---------------------------------------------------------------------------------------------

# q2. Check whether a number is prime using a loop.

# num = int(input("Enter a number : "))

# if num < 2:
#     print(f"{num} is not a prime number!")
# else:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

# if prime:
#     print(f"{num} is a prime number!")
# else:
#     print(f"{num} is not a prime number!")

# -----------------------------------------------------------------------------------------

# q3. Find the factorial of a number using a loop.

# num = int(input("Enter a number : "))
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(f"The factorial of {num} is {fact}")
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter your guess : "))
        if guess > random_number:
            print(f"The number {guess} is higher, Guess again!")
        elif guess < random_number:
            print(f"The number {guess} is lower, Guess again!")
    print(f"Your guess of number {guess} is right!!!")

guess(10)
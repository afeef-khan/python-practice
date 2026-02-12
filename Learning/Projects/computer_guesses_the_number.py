import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low
        
        feedback = input(f"The guess is {guess}, and it is:\nHigh\nLow OR\nCorrect\n")

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The guess of number {guess} was CORRECT!!!")

comp_guess(100)
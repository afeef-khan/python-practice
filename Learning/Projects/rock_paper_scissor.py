import random

def play():
    user = input("What's your choice?\nR = Rock\nP = Paper\nS = Scissor\n").upper()
    computer = random.choice(["R", "P", "S"])

    if user == computer:
        print(f"Both chose {user}. It's a TIE🤷‍♀️")
    elif won(user, computer):
        print(f"You WON😍\nComputer chose {computer} and you chose {user}")
    else:
        print(f"You Lost😢\nComputer chose {computer} and you chose {user}")

def won(player, opponent):
    return (
        (player == "R" and opponent == "S") or
        (player == "S" and opponent == "P") or
        (player == "P" and opponent == "R")
    )

play()

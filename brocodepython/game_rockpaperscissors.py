import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if player == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You loose")
        if player == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "rock":
        if player == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You loose")
        if player == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "scissors":
        if player == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You loose")
        if player == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "paper":
        if player == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You loose")
        if player == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    play_again  = input("Play  again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!!")
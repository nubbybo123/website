import random

alist = ["rock","paper","scissors"]
computer_action = random.choice(alist)
user_action = input("Enter rock, paper, or scissors. cmon i dont have all day!")

if user_action == computer_action:
    print("dude how did u tie?!")
if user_action == "scissors":
    if computer_action == "paper":
        print("congrats i guess, you won")
    else:
        print("cmon man how did you lose to a bot! do better!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("congrats i guess, you won")
    else:
        print("cmon man how did you lose to a bot! do better!")
if user_action == "paper":
    if computer_action == "rock":
        print("congrats i guess, you won")
    else:
        print("cmon man how did you lose to a bot! do better")
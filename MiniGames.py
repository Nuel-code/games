import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissors"]
while True:
    user_input = input("rock/ paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue

    rn = random.randint(0, 2)
    computer_pics = option[rn]
    print("computer chose",  computer_pics)

    if user_input == "paper" and computer_pics == "roc":
        print("you won")
        user_wins += 1

    elif user_input == "rock" and computer_pics == "scissors":
        print("you won")
        user_wins += 1

    elif user_input == "scissors" and computer_pics == "paper":
        print("you won")
        user_wins += 1

    elif user_input == computer_pics:
        print("its a draw")
        user_wins += 0
    else:
        print("you lost")
        computer_wins += 1

print("u have won", user_wins, "time")
print("computer has won", computer_wins, "time")

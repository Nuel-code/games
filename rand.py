import random
number = input("type a number: ")
if number.isdigit():
    number = int(number)
    if number <= 0:
        print("type in a number more than zero")
        quit()
else:
    print("type in a digit u")
    quit()

r = random.randrange(number)
guess = 0

while True:
    guess += 1
    your_guess = input("Guess: ")
    if your_guess.isdigit():
        your_guess = int(your_guess)
    else:
        print("type in a digit u")
        continue

    if your_guess == r:
        print("you got it right")
        break
    elif your_guess < r:
        print("go higher")
    else:
        print("go lower")

print("you got it in", guess,"guesses")







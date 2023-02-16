import random

numbers = [i for i in range(1,101)]
pick = numbers[random.randrange(0, 100)]
guess = int(input("Guess my number: "))


def try_again():
    global guess
    guess = int(input("Try again: "))
    your_guess()


def your_guess():
    global guess
    global pick
    global tries
    if guess == pick:
        print(f"Spot on! It's {pick}")
    elif guess > pick:
        print("My number is lower")
        try_again()
    elif guess < pick:
        print("My number is higher")
        try_again()



your_guess()
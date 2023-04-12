import random

while True:
    level_str = input("Enter a level (a positive integer): ")
    try:
        level = int(level_str)
        if level <= 0:
            print("Sorry! Invalid input. Please enter a positive integer.")
            continue
        else:
            break
    except ValueError:
        print("Sorry! Invalid input. Please enter a positive integer.")

num = random.randint(1, level)

while True:
    guessStr = input("Guess a number between 1 and {}: ".format(level))
    try:
        guess = int(guessStr)
        if guess <= 0:
            print("Invalid input. Please enter a positive integer.")
        elif guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Sorry! Invalid input. Please enter a positive integer.")
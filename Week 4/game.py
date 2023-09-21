import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = random.randrange(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                sys.exit("Just right!")
    except ValueError:
        pass

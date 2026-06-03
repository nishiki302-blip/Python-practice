"""
Prompt the user for a level,n.If the user does not input a positive integer,
the program should prompt again.

Randomly generates an integer between 1 and n,inclusive,using the random module.

Prompt the user to guess that integer.
If the guess is not a positive integer,the program should prompt again.
If the guess is smaller than that integer, output 'Too small!' and prompt again.
If the guess is larger than that integer, output 'Too large!' and prompt again.
If the guess is the same as that integer, output 'Just right!' and exit.
"""

from random import randint


def main():

    level = get_int("Level: ")
    guess(level)


def get_int(label="Input: "):
    while True:
        try:
            n = int(input(label))
            if n < 1:
                continue
            return n

        except ValueError:
            pass


def guess(n):
    ranValue = randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue

            elif guess < ranValue:
                print("Too small!")
                continue

            elif guess > ranValue:
                print("Too large!")
                continue

            print("Just right!")
            break

        except ValueError:
            pass


if __name__ == "__main__":
    main()

# 12 Beginner Python Projects - FreeCodeCamp
# Guess the number (Computer)

import random

def guess(x):
    random_number = random.randint(1, x)
    # This is going to return the number we need to guess
    # random.randit(a, b)
    # that returns a random integer N such that a <= N <= b
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print("Oops, not a number")
        else:
            if guess < random_number:
                print('Sorry, guess again. Too low')
            elif guess > random_number:
                print('Sorry, guess again. Too high')

        
    print(f'Yay, you got it right! It is {random_number}!')


guess(15)
#this is the range (x)

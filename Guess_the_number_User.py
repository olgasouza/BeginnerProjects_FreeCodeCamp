# 12 Beginner Python Projects - FreeCodeCamp
# Guess the number (User)

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # low == high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            # we need to adjust the upper bound
            high = guess - 1
        elif feedback == 'l':
            # adjust lower bound
            low = guess + 1

    print(f'Yay, the computer guessed your number, {guess}, correctly!')


computer_guess(10)
#this is the range (x)

# 12 Beginner Python Projects - FreeCodeCamp
# Rock Paper Scissors (Infinite loop)

import random

#rules of game
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def play():
    choices = "rps"
    user = input('Choose rock (r), papers (p) or scissors (s): ').lower()
    while user not in choices:
        user = input('Wrong input! Choose rock (r), papers (p) or scissors (s): ').lower()
    computer = random.choice(choices)
    
    print(f'you chose {user} and computer chose {computer}')
    if user == computer:
        return "It's a tie!"
    elif is_win(user, computer):
        return "You win!"
    return "You lost!"   
          
def play_again():
    resp = 'x'
    while resp.lower() != 'n':
        print(play())
        resp = input('Play again? y/n: ')
    else:
        print("Goodbye")

print(play_again())

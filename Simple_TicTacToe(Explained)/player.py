import math
import random

# =====IMPORTANT CONCEPTS=====

# SUPER() => Returns a temporary object that allows reference to a parent class.
# It saves you from rewriting methods in a subclass


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move within a given game
    def get_move(self, game):
        pass



class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        # Super() gets the info to the class 'Player'

    def get_move(self, game):
        # This will get a random open spot for the computer's next move
        square = random.choice(game.available_moves())
        return square 



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None # because the user has not inputted a value
        while not valid_square: # while it is False
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try: 
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid input, try again.')
        return val

        


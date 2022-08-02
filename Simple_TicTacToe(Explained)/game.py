from player import HumanPlayer, RandomComputerPlayer
import time


# ========IMPORTANT CONCEPTS========

# CLASS => means of bundling data and functionality together. It is like a template,
# an object constructor, or a "blue-print" for creating objects

# SELF => parameter used to access the objects within a given class

# __init__() function => All classes have this function. It can be used to assign values
# to object properties. It is called automatically everytime the class is being used to
# create a new object

# Class Person:
#   def __init__(self, name, age)
#       self.name = name
#       self.age = age

# p1 = Person(John, 36) ==> OBJECT

# The “ “.join(row) takes the board list's and converts it to a string, 
# one list element at a time, and adds a single space between each element.



# ========CREATING A BOARD========

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        # Here, I'm creating a list that will represent my 3x3 board
        # _ means each item in this list, so I'm basically saying
        # that each item in my list of 9 is ' ' (blank space)
        self.current_winner = None # this will help me keep track of winner
        # current_winner will be defined later

        # Ok, but how to we print this board?
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | '.join(row))
        # this is just setting up the rows
        # simply put, in each cycle of the loop an element of the list is created
        # therefore, since it is a list of 9, "[i*3:(i+1)*3] for i in range(3)" means that
        # the list will be organized as ([0,1,2],[3,4,5],[6,7,8]) and will be printed with
        # '|' separating each number.

    @staticmethod
    # a staticmethod eliminates the use of the self argument
    # it cannot modify object nor class state. They are restricted in the data they access.
    def print_board_nums():
    # Here I will determine which numbers correspond to each spot
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
    # range(j*3,(j+1)*3) basically means to just give the indices that are in the rows for each of the rows.
    # now I concatenate the strings the same way as above in print board
        for row in number_board:
            print(' | '.join(row))




# ========FOLLOWING THE PLAYER'S MOVES========

# Now, I have to organize two important informations:
# 1) The status of each cell in the board, to allow for next move
# 2) Each player's moves - that is, what positions are occupied by 'x' and 'o'


    def available_moves(self):
        open_moves = [] # here I'm creating an empty list
        for (i, cp) in enumerate(self.board):
            # Enumerate is going to create a list and assign tuples that have 
            # the index comma the value of that index
            # Therefore, if it is ['x', 'x', 'o'], it is going to be now [(0,'x'), (1, 'x'), (2, 'o')]
            # so i is the number of the box, and 'cp' is the player's component
            if cp == ' ':
                open_moves.append(i)
                #add the item to the end of the list, because it is available
        return open_moves

        # It can be written this way as well:
        # return [i for i,cp in enumerate(self.board) if cp == ' ']
        # which means: self.board will now be organized as a list with i,cp and if cp == ' ' then i will be returned

    def empty_squares(self):
        return ' ' in self.board 
        # It will return a Boolean, that is, it will return either True or False
        # If there are still empty spots in the board, it will return True and the game can continue.

    # Okay but how many squares are empty?
    def num_empty_squares(self):
        return self.board.count(' ')
        # this will count the numer of spaces in the board.

# The players inputs' code is displayed in more detail in 'player.py' 
# It will check if the input is valid or not by checking the available moves here.

# However, I still need to define what it means to "make a move" within the game based on the players input
    def make_move(self, square, letter):
        # if a move is valid, it will assign a square to letter (that is an input, either x or o)
        # it will then return True. If invalid, it will return False
        if self.board[square] == ' ': # remember, square is the input from either player. 
            # So this basically means that if the spot marked as the number inputted is empty... 
            # put the players letter in that box.
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

# Function to check if there is a winner:
    def winner(self, square, letter):
        # winner if 3 in a row anywhere... and all the possibilities need to be checked
        # first, check the row:
        row_ind = square // 3 # row index = which row it is at. It is going to be whatever square you give it,
        # divided by three and then rounded down. // says how many times 3 goes into square.
        row = self.board[row_ind*3:(row_ind+1)*3] # given the row index, get the row. So rows is going to be a list of
        # items in the row that we selected.
        if all([spot == letter for spot in row]): # if all the spots in that row are from a specific letter (X or O), return true
            return True
        
        # else, continue. Start verifying the columns
        col_ind = square % 3 # This is going to tell us which column we're in. % is not percentage. It divides de numbers
        # and takes the left-over.
        column = [self.board[col_ind+i*3] for i in range(3)]
        # i -> every single row | for i, if we add the column index, we essentially get every single value in that column
        # and we're gonna put that in a list. that's what [self.board[col_ind+i*3] for i in range(3)] means
        if all([spot == letter for spot in column]): # if all the spots in that column are from a specific letter (X or O), return true
            return True

        # if its false, check the diagonals
        # this is a bit harder. You only check the diagonals if the square is an even number [0, 2, 4, 6, 8]
        if square % 2 == 0: # that basically says "if the square is divisible by two..." (it is even)
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these fail, then we don't have a winner
        return False 
            

# ========STARTING THE GAME LOOP========

# Every game has some kind of loop, which runs until some player wins or the game ends in a draw.
# In TicTacToe, each loop iteration refers to a single move any player makes.
# Repetitive execution of the same block of code over and over is referred to as iteration.


def play(game, x_player, o_player, print_game=True):
    # These are variables. Each game will have a specific form, with inputs from x and o players,
    # and I want to see each move printed.
    if print_game: # ...is True
        game.print_board_nums() # then I can see which numbers correspond to each spot.

    letter = 'X' # starting letter
    # while the board still have empty spots, I want it to keep iterating.
    # When there's a winner, we can break the loop.
    while game.empty_squares(): # ...is True
        # I can get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter): # ...is valid (True), that is, if the square is empty
            if print_game: # ...is True (if I want to print the game - at the def of game)
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just empty line

            # after that move, it is necessary to alternate the letters
            # but first, I need to check if anyone won the game
            if game.current_winner: # ... is not set to None anymore
                if print_game:
                    print(letter + ' wins!')
                return letter

            # alternating letters:
            letter = 'O' if letter == 'X' else 'X'

        # tiny break
        time.sleep(0.8)

    if print_game:
        print("It's a tie!") # getting off the loop with this. 
        # because if there isn't a winner, it is a tie. 

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

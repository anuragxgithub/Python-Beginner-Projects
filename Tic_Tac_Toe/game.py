#In this version of tic tac toe there one player will be human and other will be computer itself.

#NOTE:
#1) slicing a list produces a new list containing the elements within the specified range
#2) .join() converts the iterables into a string eg ' '.join(['a', 'b', 'cd']) -> "a b cd"
#3) The enumerate function in Python is used to iterate over a sequence (such as a list, tuple,
    #or string) while keeping track of the index of the current item.

import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use the single list to rep 3x3 board
        self.current_winner = None  #Keep track of winner
        #Note the above two variables are instance variables of this class

    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]: #creates a list of lists, where each inner list represents a row of the tic-tac-toe board
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # number is having list of lists inner loops contain each row of board
        # number_board will be [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']] list of strings
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        #Looking for empty spots(' ') on board and collecting the indices of those spots
        
        return [i for (i, spot) in enumerate(self.board) if spot == ' '] #return a list of indices of empty space


    def empty_square(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move make the move (assign square to letter)
        # then return true. if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if any row column or diagonal has same letter ... we have to check all of thse.
        # check for row
        row_num = square // 3    # row & col numbering starts from 0
        row = self.board[row_num*3 : (row_num + 1)*3]  # creates a list that has a inner list which contains all the elements of that row
        if all(spot == letter for spot in row):
            return True

        # check for column
        col_num = square % 3
        col = [self.board[col_num + i*3] for i in range(3)] # creates a list of lists inner lists contains 1 element of the particular column
        if all(spot == letter for spot in col):
            return True
        
        # check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all(spot == letter for spot in diagonal1):
                return True
            diagona2 = [self.board[i] for i in [2, 4, 6]]   # right to left diagonal
            if all(spot == letter for spot in diagona2):
                return True
            
        # if everything fails
        return False
 

def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game(the letter)! or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    # iterate while game still has empty squares
    # (don't worry about the winner bcz we'll just return that which breaks the loop)
    while game.empty_square():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #lets define a fun. to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ')  #just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'   # switches player

        # tiny break to make things a litter easier to read
        time.sleep(0.8) 

    if print_game:
        print('It\'s a tie!')


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
import random

class Player:
    def __init__(self , letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):   # using inheritance
    def __init__(self, letter):
        super().__init__(letter)          #In Python, super() is a built-in function that is used to call a method from a parent class within a subclass. It's particularly useful when you're working with inheritance and want to extend or override methods from the parent class while still retaining some of their behavior. super() helps you avoid explicitly mentioning the parent class's name, making your code more maintainable and adaptable to changes.

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:   #while valid_square is false
            square =  input(self.letter + '\'s turn. Input move (0-8): ')
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        
        return val
####################################################
# FILE: ex9.py
# WRITER: Ayelet Avraham, ayeletavr, 313451932
# EXERCISE: intro2cs ex9 2019 - Rush Hour.
# DESCRIPTION: Class Game.
####################################################

from car import *
from board import *
from helper import *
import sys

class Game:

    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = Board()


    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        ERROR_MSG = 'Invalid input. Please follow game rules.'
        turn = input("Please enter your choice of car to move, and moving direction, no spaces, one comma. (example O,r)")

        #checks if input is valid:
        error = False
        if len(turn) != 3:
            print(ERROR_MSG)
            error = True
        if turn[2] != 'r' and turn[2] != 'l' and turn[2] != 'u' and turn[2] != 'd':
            print(ERROR_MSG)
            error = True
        if turn[0] not in str(self.board) or turn[0] == '-':
            print(ERROR_MSG)
            error = True

        while error:
            turn = input("Please enter your choice of car to move, and moving direction, no spaces, one comma. (example O,r)")

        self.board.move_car(turn[0], turn[1])

        print(self.board)


    def check_json_validity(self, filename):
        json_dict = load_json(filename)
        for key in json_dict:
            if key != 'Y' and key != 'B' and key != 'O' and key != 'W' and key != 'G' and key != 'R':
                return False
        for value in json_dict.values():
            if value[0] != 2 and value[0] != 3 and value[0] != 4:
                return False
            if len(value[1]) != 2 or value[1][0] not in range(7) or value[1][1] not in range(7):
                return False
            else:
                for key in json_dict:
                    car = Car(key,value[0], (value[1][0], value[1][1]), value[2])
                    self.board.add_car(car)


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while True:
            print(self.board)
            stage = self.__single_turn()
            if self.board.cell_content((3,7)) != None:
                return



if __name__ == "__main__":

    board1 = Board()
    game = Game(board1)
    Game.check_json_validity(sys.argv[0])
    game.play()

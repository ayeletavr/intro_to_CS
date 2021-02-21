####################################################
# FILE: game.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex12 2019
# DESCRIPTION: This is the file that runs 4-in-a-row game.
####################################################
from ex12.board import Board


BLUE_PLAYER = 1
RED_PLAYER = 2
ILLEGAL_MSG = "Illegal move."
BLUE_WINNER = 1
RED_WINNER = 2
TIE = 3


class Game:

    def __init__(self,):
        self.board = Board()
        self.__turns_counter = 0

    def make_move(self, column):
        """Method for one game loop. Blue player always starts."""
        if self.get_winner():
            raise Exception(ILLEGAL_MSG)
        if self.__turns_counter == 42:
            raise Exception(ILLEGAL_MSG)
        if self.get_player_at(0, column):  # to fix
            raise Exception(ILLEGAL_MSG)
        try:
            if self.get_current_player() == BLUE_PLAYER:
                self.board.add_disc(column, BLUE_PLAYER)
            elif self.get_current_player() == RED_PLAYER:
                self.board.add_disc(column, RED_PLAYER)
            self.__turns_counter += 1
        except ValueError:
            raise Exception("Not a number!")
        except IndexError:
            raise ILLEGAL_MSG

    def get_player_at(self, row, col):
        """Gets coordinate and returns which player's has a disc in it
         (or None if no one)."""
        if self.board.cell_content((row, col)) == RED_PLAYER:
            return RED_PLAYER
        elif self.board.cell_content((row, col)) == BLUE_PLAYER:
            return BLUE_PLAYER
        elif self.board.cell_content((row, col)):
            return

    def get_current_player(self):
        """Returns current player."""
        if self.__turns_counter % 2 == 0:  # if turn counter is even.
            return BLUE_PLAYER
        return RED_PLAYER

    def get_winner(self):
        """Returns the winner in game, or None if there is no winner yet."""
        blue_winner = False
        red_winner = False

        # blue player wins situations:
        # 4 blues in a row:
        for row in self.board.rows_of_board()[:3]:
            for col in self.board.cols_of_board():
                if self.get_player_at(row, col) == BLUE_PLAYER \
                        and self.get_player_at(row+1, col) == BLUE_PLAYER \
                        and self.get_player_at(row+2, col) == BLUE_PLAYER \
                        and self.get_player_at(row+3, col) == BLUE_PLAYER:
                    blue_winner = True

        # 4 blues in a col:
        for row in self.board.rows_of_board():
            for col in self.board.cols_of_board()[:2]:
                if self.get_player_at(row, col) == BLUE_PLAYER \
                        and self.get_player_at(row, col+1) == BLUE_PLAYER \
                        and self.get_player_at(row, col+2) == BLUE_PLAYER \
                        and self.get_player_at(row, col+3) == BLUE_PLAYER:
                    blue_winner = True

        # 4 blues in a going-down diagonal:
        for row in self.board.rows_of_board()[:3]:
            for col in self.board.cols_of_board()[:4]:
                if self.get_player_at(row, col) == BLUE_PLAYER \
                        and self.get_player_at(row+1, col+1) == BLUE_PLAYER \
                        and self.get_player_at(row+2, col+2) == BLUE_PLAYER \
                        and self.get_player_at(row+3, col+3) == BLUE_PLAYER:
                    blue_winner = True

        # 4 blues in a going-up diagonal:
        for row in self.board.rows_of_board()[3:]:
            for col in self.board.cols_of_board()[:3]:
                if self.get_player_at(row, col) == BLUE_PLAYER \
                        and self.get_player_at(row - 1, col + 1) ==\
                        BLUE_PLAYER \
                        and self.get_player_at(row - 2, col + 2) ==\
                        BLUE_PLAYER \
                        and self.get_player_at(row - 3, col + 3) == \
                        BLUE_PLAYER:
                    blue_winner = True

        # red player wins situations:
        # 4 reds in a row:
        for row in self.board.rows_of_board()[:3]:
            for col in self.board.cols_of_board():
                if self.get_player_at(row, col) == RED_PLAYER \
                        and self.get_player_at(row+1, col) == RED_PLAYER \
                        and self.get_player_at(row+2, col) == RED_PLAYER \
                        and self.get_player_at(row+3, col) == RED_PLAYER:
                    red_winner = True

        # 4 reds in a col:
        for row in self.board.rows_of_board():
            for col in self.board.cols_of_board()[:2]:
                if self.get_player_at(row, col) == RED_PLAYER \
                        and self.get_player_at(row, col+1) == RED_PLAYER \
                        and self.get_player_at(row, col+2) == RED_PLAYER \
                        and self.get_player_at(row, col+3) == RED_PLAYER:
                    red_winner = True

        # 4 reds in a going-down diagonal:
        for row in self.board.rows_of_board()[:3]:
            for col in self.board.cols_of_board()[:4]:
                if self.get_player_at(row, col) == RED_PLAYER \
                        and self.get_player_at(row+1, col+1) == RED_PLAYER \
                        and self.get_player_at(row+2, col+2) == RED_PLAYER \
                        and self.get_player_at(row+3, col+3) == RED_PLAYER:
                    red_winner = True

        # 4 reds in a going-up diagonal:
        for row in self.board.rows_of_board()[3:]:
            for col in self.board.cols_of_board()[:3]:
                if self.get_player_at(row, col) == RED_PLAYER \
                        and self.get_player_at(row-1, col + 1) == RED_PLAYER \
                        and self.get_player_at(row-2, col + 2) == RED_PLAYER \
                        and self.get_player_at(row-3, col + 3) == RED_PLAYER:
                    red_winner = True

        # Determine the winner:

        if blue_winner and red_winner is False:
            return BLUE_WINNER
        if red_winner and blue_winner is False:
            return RED_WINNER
        if (not blue_winner) and (not red_winner) and \
                self.__turns_counter == 42:
            return TIE
        if blue_winner is False and red_winner is False:
            return

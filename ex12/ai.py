####################################################
# FILE: ai.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex10 2019
# DESCRIPTION: file of ai.
####################################################
import random


class AI:

    def __init__(self, game):
        """
        AI constructor
        :param game:
        """
        self.__game = game

    def full_columns(self):
        """Returns a list with columns that are full to top with discs."""
        cols_lst = []
        for col in range(6):
            if self.__game.get_player_at(0, col) is not None:
                cols_lst.append(col)
        return cols_lst

    def find_legal_move(self, timeout=None):
        """
        return a random column of a not full column
        :param timeout:
        :return:
        """
        legal_cols = []
        for col in range(6):
            if col not in self.full_columns():
                legal_cols.append(col)
        return random.choice(legal_cols)

    def get_last_found_move(self):
        pass

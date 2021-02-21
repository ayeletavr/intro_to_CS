####################################################
# FILE: board.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex12 2019
# DESCRIPTION: file of class board that creates board object.
####################################################
from ex12.disc import Disc


class Board:

    def __init__(self, height=6, width=7):
        self.__height = height  # int
        self.__width = width  # int
        self.__discs = []

    def __str__(self):
        """Makes board visual, can be printed. Returns a string presents the
         current status of board."""
        # board_lst = [['-'] * self.__width for rows in range(self.__height)]
        board_lst = []
        for row in self.rows_of_board():
            row_lst = []
            for col in self.cols_of_board():
                row_lst.append('-')
            board_lst.append(row_lst)
        for disc in self.__discs:
            for coordinate in disc.get_location():
                board_lst[coordinate[0]][coordinate[1]] = str(disc.get_color())
        board_str = ""
        for row in board_lst:
            for col in row:
                board_str += col
            board_str += '\n'
        return board_str

    def rows_of_board(self):
        """returns a list of indexes of all rows."""
        rows = []
        for i in range(self.__height):
            rows.append(i)
        return rows

    def cols_of_board(self):
        """Returns a list of indexes of all columns in board."""
        cols = []
        for i in range(self.__width):
            cols.append(i)
        return cols

    def cell_content(self, coordinate):
        """First, checks if the given coordinate is empty. If true, returns
        None. Else, returns color of disc."""
        for disc in self.__discs:
            if coordinate == disc.get_location()[0]:
                return disc.get_color()

    def add_disc(self, col, color):
        """Adds a disc to board. Player can add a disc only by choosing
         a col."""
        y_coordinate = col
        if not self.__discs:  # at start, there are no discs on board.
            x_coordinate = self.__height - 1
        else:
            used_x = []
            for disc in self.__discs:
                if disc.get_location()[0][1] == col:
                    used_x.append(disc.get_location()[0][0])
                else:
                    used_x.append(self.__height)
            min_x = min(used_x)
            x_coordinate = min_x - 1
        disc = Disc(color, x_coordinate, y_coordinate)
        self.__discs.append(disc)

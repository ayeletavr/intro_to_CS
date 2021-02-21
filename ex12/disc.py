####################################################
# FILE: disc.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex12 2019
# DESCRIPTION: file of class disc that creates disc object.
####################################################


class Disc:

    def __init__(self, color, x_coordinate, y_coordinate):
        """Constructor to disc"""
        self.__color = color
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

# Getters and Setters
    def get_color(self):
        """Color getter."""
        return self.__color

    def get_location(self):
        """Disc's location getter."""
        return [(self.__x_coordinate, self.__y_coordinate)]













"""
class Chips:

    CHIP_TYPES = ['red', 'blue']

    

    def __init__(self):
        
        initialize a chip object

        
        self._chips = {}

    def add_chip(self, color, cords):
        
        :param color: from CHIP_TYPES
        :param cords: from CHIP_LAYOUT
        :return:
        
        self._chips[cords] = color

    def get_chips_dict(self):
        
        Returns a dict of all chips in the format of (coordinates, color)
        
        return self._chips
"""



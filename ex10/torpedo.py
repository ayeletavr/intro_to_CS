####################################################
# FILE: torpedo.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex10 2019
# DESCRIPTION: torpedo object file.
####################################################

class Torpedo:
    def __init__(self, x_coordinate, y_coordinate, x_velocity, y_velocity, heading, life_span=0):
        """This class contains torpedo object, and also special torpedo."""
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__x_velocity = x_velocity
        self.__y_velocity = y_velocity
        self.__heading = heading
        self.__life_span = life_span  # for stage D, mission 5

    def get_x_coordinate(self):
        """Returns torpedo X coordinate."""
        return self.__x_coordinate

    def get_y_coordinate(self):
        """Returns torpedo Y location."""
        return self.__y_coordinate

    def get_heading(self):
        """Returns torpedo heading."""
        return self.__heading

    def get_life_span(self):
        """Returns torpedo's life span."""
        return self.__life_span

    def update_life_span(self):
        """Adds a life."""
        self.__life_span += 1

    def get_radius(self):
        """Returns torpedo radius"""
        return 4

    def get_x_velocity(self):
        """"Returns torpedo x velocity."""
        return self.__x_velocity

    def get_y_velocity(self):
        """Returns torpedo y speed."""
        return self.__y_velocity

    def move_torpedo(self, screen_min_x, screen_max_x, screen_min_y, screen_max_y):
        """Changes location of torpedo."""
        self.__x_coordinate = (self.__x_velocity + self.__x_coordinate - screen_min_x)\
                              % (screen_max_x - screen_min_x) + screen_min_x
        self.__y_coordinate = (self.__y_velocity + self.__y_coordinate - screen_min_y)\
                              % (screen_max_y - screen_min_y) + screen_min_y

    def move_special_torpedoe(self, screen_min_x, screen_max_x, screen_min_y, screen_max_y):
        """Changes location of special torpedo."""
        self.__x_coordinate = 3*(self.__x_velocity + self.__x_coordinate - screen_min_x)\
                              % (screen_max_x - screen_min_x) + screen_min_x
        self.__y_coordinate = 3*(self.__y_velocity + self.__y_coordinate - screen_min_y)\
                              % (screen_max_y - screen_min_y) + screen_min_y
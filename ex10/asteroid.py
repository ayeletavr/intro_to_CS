####################################################
# FILE: asteroid.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex10 2019
# DESCRIPTION: asteroid object file.
####################################################


class Asteroid:
    def __init__(self, x_coordinate, y_coordinate, x_velocity, y_velocity, size):
        """This class contains asteroid object.
         There are many of them in the game, and the mission is to explode them."""
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__x_velocity = x_velocity
        self.__y_velocity = y_velocity
        self.__size = size

    def has_intersection(self, obj):
        """
        two asteroids can be in the same coordinates without colliding
        """
        distance = ((obj.get_x_coordinate() - self.__x_coordinate) ** 2 +
                    (obj.get_y_coordinate() - self.__y_coordinate) ** 2) ** 0.5
        asteroid_radius = self.__size * 10 - 5  # 10 is the size coefficient,
        # 5 is the normalization coefficient
        if distance <= asteroid_radius + obj.get_radius():
            return True
        return False

    def get_x_coordinate(self):
        """Returns asteroid's X coordinate."""
        return self.__x_coordinate

    def get_y_coordinate(self):
        """Returns asteroid's Y coordinate."""
        return self.__y_coordinate

    def get_size(self):
        """Returns Asteroid's size."""
        return self.__size

    def set_size(self, size):
        """Changes asteroid's size to 1 (for the special torpedo activation."""
        self.__size = size

    def get_x_velocity(self):
        """Returns asteroid's x axis velocity."""
        return self.__x_velocity

    def get_y_velocity(self):
        """Returns asteroid's y axis velocity."""
        return self.__y_velocity

    def move_asteroid(self, screen_min_x, screen_max_x, screen_min_y, screen_max_y):
        """Changes location of asteroid."""
        self.__x_coordinate = (self.__x_velocity + self.__x_coordinate - screen_min_x) % (screen_max_x - screen_min_x) + screen_min_x
        self.__y_coordinate = (self.__y_velocity + self.__y_coordinate - screen_min_y) % (screen_max_y - screen_min_y) + screen_min_y

    def get_radius(self):
        """Returns asteroid's radius."""
        return self.__size * 10 - 5
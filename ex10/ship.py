####################################################
# FILE: ship.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex10 2019
# DESCRIPTION: ship object file.
####################################################

import math
import random

class Ship:
    """
    This is class ship contains ship object. The ship is the player in our game.
    """
    def __init__(self, x_coordinate, y_coordinate, x_velocity, y_velocity, heading):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__x_velocity = x_velocity
        self.__y_velocity = y_velocity
        self.__heading = heading

    def get_x_coordinate(self):
        """Returns ship's X coordinate"""
        return self.__x_coordinate

    def get_y_coordinate(self):
        """Returns ship's Y coordinate"""
        return self.__y_coordinate

    def get_heading(self):
        """Returns ship heading"""
        return self.__heading

    def get_heading_in_radians(self):
        """Returns ship's heading in radians."""
        return (self.__heading * math.pi) / 180

    def get_x_velocity(self):
        """Returns ship's x axis velocity."""
        return self.__x_velocity

    def get_y_velocity(self):
        """Returns ship's y axis velocity."""
        return self.__y_velocity

    def move_ship(self, screen_min_x, screen_max_x, screen_min_y, screen_max_y):
        """Changes location of ship."""
        self.__x_coordinate = (self.__x_velocity + self.__x_coordinate - screen_min_x) % \
                              (screen_max_x - screen_min_x) + screen_min_x
        self.__y_coordinate = (self.__y_velocity + self.__y_coordinate - screen_min_y) % \
                              (screen_max_y - screen_min_y) + screen_min_y

    def turn_ship_right(self):
        """Turns ship clockwise."""
        self.__heading += 7

    def turn_ship_left(self):
        """Turns ship against clockwise."""
        self.__heading -= 7

    def accelerate_ship(self):
        """Accelerate ship's velocity."""
        # to change angle from degrees to radians:
        degrees_in_pi_radian = 180
        heading_in_radians = (self.__heading * math.pi) / degrees_in_pi_radian

        self.__x_velocity = self.__x_velocity + math.cos(heading_in_radians)
        self.__y_velocity = self.__y_velocity + math.sin(heading_in_radians)

    def get_radius(self):
        """Returns ship's radius."""
        return 1

    def teleport_ship(self, screen_min_x, screen_max_x, screen_min_y, screen_max_y, astroids):
        """
        changes ship's coordinates to a random location on screen, without colliding with an asteroid.
        """
        not_collide = False
        while not_collide == False:
            new_x_coordinate = random.randint(screen_min_x, screen_max_x)
            new_y_coordinate = random.randint(screen_min_y, screen_max_y)
            # check if new coordinates don't ake a collision with an asteroid:
            for asteroid in astroids:
                if asteroid.get_x_coordinate() == new_x_coordinate:
                    not_collide = False
                elif asteroid.get_y_coordinate() == new_y_coordinate:
                    not_collide = False
                else:
                    not_collide = True
        self.__x_coordinate = new_x_coordinate
        self.__y_coordinate = new_y_coordinate
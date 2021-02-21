####################################################
# FILE: ex9.py
# WRITER: Ayelet Avraham, ayeletavr, 313451932
# EXERCISE: intro2cs ex9 2019 - Rush Hour.
# DESCRIPTION: Class Car.
####################################################

from helper import *

class Car:
    """
    Car class represent all cars. this class doesn't aware of other classes in the game.
    """
    MOVEMENTS = 'r', 'l', 'u', 'd'
    RIGHT, LEFT, UP, DOWN = MOVEMENTS
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates = []
        if self.__orientation == 0: #if car is vertical.
            for i in range(self.__location[0],self.__length+self.__location[0]):
                coordinates.append((i, self.__location[1]))
        elif self.__orientation == 1: #if car is horizonal.
            for i in range(self.__location[1],self.__length+self.__location[1]):
                coordinates.append((self.__location[0],i))
        return coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.__orientation == 0:
            result = {'u': "Go up", 'd': "Go down"}
        else: #self.__orientation == 1:
            result = {'l': "Go left", 'r': "Go right"}
        return result

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        #If car is vertical:
        if self.__orientation == 0 and movekey == 'd':
            return [(self.car_coordinates()[-1][0]+1, self.car_coordinates()[-1][1])]
        if self.__orientation == 0 and movekey == 'u':
            return [(self.car_coordinates()[0][0]-1, self.car_coordinates()[0][1])]

        #If car is horizonal:
        if self.__orientation == 1 and movekey == 'r':
            return [(self.car_coordinates()[-1][0], self.car_coordinates()[-1][1]+1)]
        if self.__orientation == 1 and movekey == 'l':
            return [(self.car_coordinates()[0][0], self.car_coordinates()[0][1]-1)]


    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey == Car.UP and self.__orientation == 0:
            self.__location = (self.__location[0]-1, self.__location[1])
            return True
        elif movekey == Car.DOWN and self.__orientation == 0:
            self.__location = (self.__location[0]+1, self.__location[1])
            return True
        elif movekey == Car.RIGHT and self.__orientation == 1:
            self.__location = (self.__location[0], self.__location[1]+1)
            return True
        elif movekey == Car.LEFT and self.__orientation == 1:
            self.__location = (self.__location[0], self.__location[1]-1)
            return True
        else: return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name

####################################################
# FILE: ex9.py
# WRITER: Ayelet Avraham, ayeletavr, 313451932
# EXERCISE: intro2cs ex9 2019 - Rush Hour.
# DESCRIPTION: Class Board.
####################################################

from car import *
class Board:
    """
    This class represent boards of the game. there is one default board (7*7), and one escape coordinate.
    Board class has to know Car class in order to place cars on board.
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__height = 7
        self.__width = 7
        self.__cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        #The game may assume this function returns a reasonable representation
        #of the board for printing, but may not assume details about it.
        board_lists = [['-'] * self.__width for rows in range(self.__height)]
        for car in self.__cars:
            for coordinate in car.car_coordinates():
                board_lists[coordinate[0]][coordinate[1]] = str(car.get_name())
        board_str = ""
        for row in board_lists:
            for col in row:
                board_str += col
            board_str += '\n'
        return board_str


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        cells = []
        for i in range(self.__height):
            for j in range(self.__width):
                cell = (i,j)
                cells.append(cell)
        TARGET_CELL = (3,7)
        cells.append(TARGET_CELL)
        return cells


    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.__cars:
            if coordinate in car.car_coordinates():
                return car.get_name()
            else: return None


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        result = []
        for car in self.__cars:
            if 'r' in car.possible_moves().keys() \
                    and car.movement_requirements('r')[0][0] in range(self.__height) \
                and car.movement_requirements('r')[0][1] in range(self.__width)\
                    and self.cell_content((car.car_coordinates()[-1][0], car.car_coordinates()[-1][1]+1)) == None:
                tup = (car.get_name(), 'r', "You can move right.")
                result.append(tup)
            if 'l' in car.possible_moves().keys() \
                    and car.movement_requirements('l')[0][0] in range(self.__height) \
                    and car.movement_requirements('l')[0][1] in range(self.__width) \
                    and self.cell_content((car.car_coordinates()[0][0], car.car_coordinates()[0][1]-1)) == None:
                tup = (car.get_name(), 'l', "You can move left.")
                result.append(tup)
            if 'u' in car.possible_moves().keys() \
                    and car.movement_requirements('u')[0][0] in range(self.__height)\
                    and car.movement_requirements('u')[0][1] in range(self.__width)\
                    and self.cell_content((car.car_coordinates()[0][0]-1, car.car_coordinates()[0][1])) == None:
                tup = (car.get_name(), 'u', "You can move up.")
                result.append(tup)
            if 'd' in car.possible_moves().keys() \
                    and car.movement_requirements('d')[0][0] in range(self.__height) \
                    and car.movement_requirements('d')[0][1] in range(self.__width)\
                    and self.cell_content((car.car_coordinates()[-1][0]+1, car.car_coordinates()[-1][1])) == None:
                tup = (car.get_name(), 'd', "You can move down.")
                result.append(tup)
        return result


    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        return (3,7)


    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for coordinate in car.car_coordinates():

            #check if empty:
            if self.cell_content(coordinate) != None:
                return False
            self.__cars.append(car)
            return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if self.__cars == []:
            return False
        else:
            for car in self.__cars:
                if name == car.get_name():
                    car.move(movekey)
                    return True
                else:
                    return False

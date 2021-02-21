####################################################
# FILE: asteroids_main.py
# WRITERS: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex10 2019
# DESCRIPTION: This is the file that runs asteroids game.
####################################################
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import sys
import random
import math

DEFAULT_ASTEROIDS_NUM = 5
INIT_X = random.randint(Screen.SCREEN_MIN_X,Screen.SCREEN_MAX_X)
INIT_Y = random.randint(Screen.SCREEN_MIN_Y,Screen.SCREEN_MAX_Y)
EXCLUDE_INIT_X = range(Screen.SCREEN_MIN_X, INIT_X) and range(INIT_X+1, Screen.SCREEN_MAX_X)
INIT_ASTEROID_X = random.choice(EXCLUDE_INIT_X)
EXCLUDE_INIT_Y = range(Screen.SCREEN_MIN_Y, INIT_Y) and range(INIT_Y+1, Screen.SCREEN_MAX_Y)
INIT_ASTEROID_Y = random.choice(EXCLUDE_INIT_Y)
INIT_ASTEROID_SIZE = 3
ASTEROID_VELOCITIES = [1, 2, 3, 4, -1, -2, -3, -4]
MAX_TORPEDOES = 10
MAX_SPECIAL_TORPEDOES = 5
INIT_SCORES = 0
ACCELERATION_COEFFICIENT = 2

class GameRunner:

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        """This is the init of GameRunner."""
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__screen_ship = Ship(INIT_X, INIT_Y, 0, 0, 0)
        self.__screen_asteroids = []
        self.__screen_asteroids_amount = asteroids_amount
        for i in range(asteroids_amount):
            x_coordinate = INIT_ASTEROID_X
            y_coordinate = INIT_ASTEROID_Y
            x_velocity = random.choice(ASTEROID_VELOCITIES)
            y_velocity = random.choice(ASTEROID_VELOCITIES)
            size = INIT_ASTEROID_SIZE
            new_asteroid = Asteroid(x_coordinate, y_coordinate, x_velocity, y_velocity, size)
            self.__screen.register_asteroid(new_asteroid, size)
            self.__screen_asteroids.append(new_asteroid)
        self.__screen_torpedoes = []
        self.__screen_special_torpedoes = []
        self.__score = INIT_SCORES

    def ship_asteroid_collide(self):
        """When ship and asteroid collides, the asteroid disappears but ship loses one life."""
        for asteroid in self.__screen_asteroids:

            if asteroid.has_intersection(self.__screen_ship):
                self.__screen.show_message(
                    title="collision",
                    msg=" Ouch! you collided an asteroid! -1 life")
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                self.__screen_asteroids.remove(asteroid)  # remove from list.
                break
                # remove the guilty asteroid

    def split_asteroid(self, asteroid, torpedo):
        """split an asteroid as described when being hit by a torpedo"""
        if asteroid.get_size() == 3:  # split to two fragments of size 2, that go in different directions,
            # according to a given formula
            fragment_1_x_vel = (torpedo.get_x_velocity() + asteroid.get_x_velocity()) \
                               / (asteroid.get_x_velocity() ** 2 + asteroid.get_y_velocity() ** 2) ** 0.5
            fragment_1_y_vel = (torpedo.get_y_velocity() + asteroid.get_y_velocity()) \
                               / (asteroid.get_x_velocity() ** 2 + asteroid.get_y_velocity() ** 2) ** 0.5
            fragment_1 = Asteroid(asteroid.get_x_coordinate(), asteroid.get_y_coordinate(),
                                  fragment_1_x_vel, fragment_1_y_vel, size=2)  # of size 2
            self.__screen.register_asteroid(fragment_1, fragment_1.get_size())
            self.__screen_asteroids.append(fragment_1)

            fragment_2_x_vel = (torpedo.get_x_velocity() + (-1)*asteroid.get_x_velocity()) \
                               / (((-1)*asteroid.get_x_velocity()) ** 2 + ((-1)*asteroid.get_y_velocity()) ** 2) ** 0.5
            # asteroid multiplied by -1 so the fragments go in opposite directions
            fragment_2_y_vel = (torpedo.get_y_velocity() + (-1)*asteroid.get_y_velocity()) \
                               / (((-1)*asteroid.get_x_velocity()) ** 2 + ((-1)*asteroid.get_y_velocity()) ** 2) ** 0.5  # asteroid multiplied by -1 so the fragments go in opposite directions
            fragment_2 = Asteroid(asteroid.get_x_coordinate(), asteroid.get_y_coordinate(),
                                  fragment_2_x_vel, fragment_2_y_vel, size=2)  # of size 2
            self.__screen.register_asteroid(fragment_2, fragment_2.get_size())
            self.__screen_asteroids.append(fragment_2)

        if asteroid.get_size() == 2:  # split to two fragments of size 1,
            # that go in different directions, according to a given formula
            fragment_1_x_vel = (torpedo.get_x_velocity() + asteroid.get_x_velocity()) \
                               / (asteroid.get_x_velocity() ** 2 +
                                                                             asteroid.get_y_velocity() ** 2) ** 0.5
            fragment_1_y_vel = (torpedo.get_y_velocity() + asteroid.get_y_velocity()) \
                               / (asteroid.get_x_velocity() ** 2 +
                                                                                 asteroid.get_y_velocity() ** 2) ** 0.5
            fragment_1 = Asteroid(asteroid.get_x_coordinate(), asteroid.get_y_coordinate(),
                                  fragment_1_x_vel, fragment_1_y_vel, size=1)  # of size 1
            self.__screen.register_asteroid(fragment_1, fragment_1.get_size())
            self.__screen_asteroids.append(fragment_1)

            fragment_2_x_vel = \
                (torpedo.get_x_velocity() + (-1)*asteroid.get_x_velocity()) /\
                (((-1)*asteroid.get_x_velocity()) ** 2 + ((-1)*asteroid.get_y_velocity()) ** 2) ** 0.5
            # asteroid multiplied by -1 so the fragments go in opposite directions
            fragment_2_y_vel =\
                (torpedo.get_y_velocity() + (-1)*asteroid.get_y_velocity()) /\
                (((-1)*asteroid.get_x_velocity()) ** 2 + ((-1)*asteroid.get_y_velocity()) ** 2) ** 0.5
            # asteroid multiplied by -1 so the fragments go in opposite directions
            fragment_2 = Asteroid(asteroid.get_x_coordinate(), asteroid.get_y_coordinate(),
                                  fragment_2_x_vel, fragment_2_y_vel, size=1)  # of size 1
            self.__screen.register_asteroid(fragment_2, fragment_2.get_size())
            self.__screen_asteroids.append(fragment_2)

        self.__screen.unregister_asteroid(asteroid)
        self.__screen_asteroids.remove(asteroid)  # remove the original asteroid from list.

        #  asteroid of size 1 disappears without splitting
        # self.__screen.unregister_asteroid(asteroid)  # remove the old asteroid from the screen

    def torpedo_asteroid_collide(self):
        """
        the radius of a torpedo is 4
        the asteroid explodes, but does not disappear( splits)
        ADD POINTS TO THE CURRENT SCORE AS DESCRIBED
        """
        for torpedo in self.__screen_torpedoes:
            for asteroid in self.__screen_asteroids:

                if asteroid.has_intersection(torpedo):
                    self.__screen.show_message(
                        title="hit",
                        msg=" You hit an asteroid! boom-boom-boom")
                # add points according to asteroid size: size 3 = 20 pts, size 2 = 50 pts, size 1 = 100 pts
                    if asteroid.get_size() == 3:
                        self.__screen.set_score(self.__score + 20)
                        self.__score += 20
                    if asteroid.get_size() == 2:
                        self.__screen.set_score(self.__score + 50)
                        self.__score += 50
                    if asteroid.get_size() == 1:
                        self.__screen.set_score(self.__score + 100)
                        self.__score += 100
                    self.split_asteroid(asteroid, torpedo)  # the asteroid explodes - split it
                    self.__screen.unregister_torpedo(torpedo)  # remove the torpedo from the screen
                    self.__screen_torpedoes.remove(torpedo)

    def add_torpedo(self):
        """
        initial heading and location are those of the ship, and initial velocity as described.
        """
        x_coordinate = self.__screen_ship.get_x_coordinate()
        y_coordinate = self.__screen_ship.get_y_coordinate()
        heading = self.__screen_ship.get_heading_in_radians()
        new_x_velocity = self.__screen_ship.get_x_velocity() + ACCELERATION_COEFFICIENT * math.cos(heading)
        new_y_velocity = self.__screen_ship.get_y_velocity() + ACCELERATION_COEFFICIENT * math.sin(heading)
        new_torpedo = Torpedo(x_coordinate, y_coordinate, new_x_velocity, new_y_velocity, heading)
        self.__screen.register_torpedo(new_torpedo)
        self.__screen_torpedoes.append(new_torpedo)

    def torpedo_life_span(self):
        """
        each torpedo has a life span of 200 game loops.
        call this function at each loop for each torpedo.
        """
        for torpedo in self.__screen_torpedoes:
            if torpedo.get_life_span == 200:
                self.__screen.unregister_torpedo(torpedo)
                self.__screen_torpedoes.remove(torpedo)
            torpedo.update_life_span()

    def move_objects(self):
        """This function updates locations of all objects n the game."""
        self.__screen_ship.move_ship(self.__screen_min_x, self.__screen_max_x, self.__screen_min_y, self.__screen_max_y)
        for asteroid in self.__screen_asteroids:
            asteroid.move_asteroid(self.__screen_min_x, self.__screen_max_x, self.__screen_min_y, self.__screen_max_y)
        for torpedo in self.__screen_torpedoes:
            torpedo.move_torpedo(self.__screen_min_x, self.__screen_max_x, self.__screen_min_y, self.__screen_max_y)
        for torpedo in self.__screen_special_torpedoes:
            torpedo.move_torpedo(self.__screen_min_x, self.__screen_max_x, self.__screen_min_y, self.__screen_max_y)

    def check_input(self):
        """Checks user's input and responds."""
        if self.__screen.is_left_pressed():
            self.__screen_ship.turn_ship_right()
        if self.__screen.is_right_pressed():
            self.__screen_ship.turn_ship_left()
        if self.__screen.is_up_pressed():
            self.__screen_ship.accelerate_ship()
        if self.__screen.is_space_pressed():
            if len(self.__screen_torpedoes) < MAX_TORPEDOES:
                self.add_torpedo()
        if self.__screen.is_teleport_pressed():
            self.__screen_ship.teleport_ship(self.__screen_min_x, self.__screen_max_x,
                                             self.__screen_min_y, self.__screen_max_y, self.__screen_asteroids)
        if self.__screen.is_special_pressed():
            if len(self.__screen_special_torpedoes) < MAX_SPECIAL_TORPEDOES:
                self.add_special_torpedo()

    def draw_ship(self):
        """Draw ship on screen."""
        x_coordinate = self.__screen_ship.get_x_coordinate()
        y_coordinate = self.__screen_ship.get_y_coordinate()
        heading = self.__screen_ship.get_heading()
        self.__screen.draw_ship(x_coordinate, y_coordinate, heading)

    def draw_asteroid(self):
        """For each asteroid in the game, draw it on screen."""
        for asteroid in self.__screen_asteroids:
            x_coordinate = asteroid.get_x_coordinate()
            y_coordinate = asteroid.get_y_coordinate()
            self.__screen.draw_asteroid(asteroid, x_coordinate, y_coordinate)

    def draw_torpedo(self):
        """Draw torpedo on screen"""
        for torpedo in self.__screen_torpedoes:
            x_location = torpedo.get_x_coordinate()
            y_location = torpedo.get_y_coordinate()
            heading = torpedo.get_heading()
            self.__screen.draw_torpedo(torpedo, x_location, y_location, heading)

    def draw_special_torpedo(self):
        """Draw special torpedo on screen."""
        for torpedo in self.__screen_special_torpedoes:
            x_location = torpedo.get_x_coordinate()
            y_location = torpedo.get_y_coordinate()
            heading = torpedo.get_heading()
            self.__screen.draw_torpedo(torpedo, x_location, y_location, heading)

    def draw_objects_on_screen(self):
        """Draws all objects on screen."""
        self.draw_ship()
        self.draw_asteroid()
        self.draw_torpedo()
        self.draw_special_torpedo()

    def end_game(self):
        """
        relevant situations:
        1- all asteroids destroyed
        2- ship is destroyed (0 life)
        3- quit button ('q') was pressed

        return True if the game should end and False otherwise
        :return: boolean
        """
        if self.__screen_asteroids == []:  # indication 1, it means the list is empty
            self.__screen.show_message("win msg", "Yow won the game!")
            self.__screen.end_game()
        if self.torpedo_life_span() == 0:  # indication 2,  ADD THIS ATTRIBUTE TO THE SHIP
            self.__screen.show_message("Lost msg" "No more life for you :( Maybe next time...")
            self.__screen.end_game()
        if self.__screen.should_end():  # if True then 'q' is pressed
            self.__screen.show_message("Exit game", "You must have something very important to do now.")
            self.__screen.end_game()
        return False


    def add_special_torpedo(self): # it's a torpedo with an endless lifespan
        """
        the torpedoes velocity remains constant
        initial heading and location are those of the ship
        """
        x_coordinate = self.__screen_ship.get_x_coordinate()
        y_coordinate = self.__screen_ship.get_y_coordinate()
        heading = self.__screen_ship.get_heading_in_radians()
        new_x_velocity = self.__screen_ship.get_x_velocity() + 2 * math.cos(heading)  # 2 is the acceleration coefficient
        new_y_velocity = self.__screen_ship.get_y_velocity() + 2 * math.sin(heading)
        new_torpedo = Torpedo(x_coordinate, y_coordinate, new_x_velocity, new_y_velocity, heading)
        self.__screen_special_torpedoes.append(new_torpedo)
        self.__screen.register_torpedo(new_torpedo)

    def special_torpedo_asteroid_collide(self):
        """
        the radius of a torpedo is 4
        the special torpedo makes any asteroid disappear and rewards th eplayer with 1000 points!
        also, it has an endless lifespan, and it's velocity is 3 times faster than the regular torpedo.
        """
        for torpedo in self.__screen_special_torpedoes:
            for asteroid in self.__screen_asteroids:
                if asteroid.has_intersection(torpedo):
                    self.__screen.show_message(
                        title="special hit",
                        msg=" You hit an asteroid! boom-boom-boom! pow-pow! shabang!")
                    # add points according to asteroid size: size 3 = 20 pts, size 2 = 50 pts, size 1 = 100 pts
                    if asteroid.get_size() == 3:
                        self.__screen.set_score(self.__score + 1000)
                        self.__score += 1000
                    if asteroid.get_size() == 2:
                        self.__screen.set_score(self.__score + 1000)
                        self.__score += 1000
                    if asteroid.get_size() == 1:
                        self.__screen.set_score(self.__score + 1000)
                        self.__score += 1000
                    asteroid.set_size(1)  # we made it of size 1 so it will disappear without fragments
                    self.split_asteroid(asteroid, torpedo)  # the asteroid explodes - split it
                    self.__screen.unregister_torpedo(torpedo)  # remove the torpedo from the screen
                    self.__screen_special_torpedoes.remove(torpedo)

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """This function runs one game loop."""
        self.end_game()
        self.move_objects()
        self.torpedo_life_span()
        self.check_input()
        self.draw_objects_on_screen()
        self.ship_asteroid_collide()
        self.torpedo_asteroid_collide()
        self.special_torpedo_asteroid_collide()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)

####################################################
# FILE: gui_module.py
# WRITER: Golan Shany; golans, Ayelet Avraham; ayeletavr
# EXERCISE: intro2cs ex12 2019
# DESCRIPTION: the gui module of our game
####################################################

import tkinter as tk
from tkinter import messagebox
from ex12.game import *
from ex12.ai import *

DISCS_LAYOUT = [[(50, 550), (50, 450), (50, 350), (50, 250), (50, 150),
                 (50, 50)],
                   [(150, 550), (150, 450), (150, 350), (150, 250), (150, 150),
                    (150, 50)],
                   [(250, 550), (250, 450), (250, 350), (250, 250), (250, 150),
                    (250, 50)],
                   [(350, 550), (350, 450), (350, 350), (350, 250), (350, 150),
                    (350, 50)],
                   [(450, 550), (450, 450), (450, 350), (450, 250), (450, 150),
                    (450, 50)],
                   [(550, 550), (550, 450), (550, 350), (550, 250), (550, 150),
                    (550, 50)],
                   [(650, 550), (650, 450), (650, 350), (650, 250), (650, 150),
                    (650, 50)]]  # [column][row]


class Screen:

    def __init__(self):
        """
        initiate graphics class.
        """
        # set game parameters

        self.game = Game()
        self.ai = AI(self.game)
        self.col_ind = [0, 0, 0, 0, 0, 0, 0]
        self.start = False
        self.player1 = None
        self.player2 = None
        self._victories = []
        self.player_turn = "blue"  # means when the game starts it's
        # blue player's turn
        # set tkinter's basics
        # creating the main window
        self._root = tk.Tk()
        self._root.title("Four in a Row")
        # root key binding
        self._root.bind("1", self.player1_human)
        self._root.bind("2", self.player1_virtual)
        self._root.bind("3", self.player2_human)
        self._root.bind("4", self.player2_virtual)
        self._root.bind('<Return>', self.set_start)

        # adding frame widget
        self.frame = tk.Frame(self._root, bg='lightblue')
        self.frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # adding button widgets
        quit_button = tk.Button(self.frame, text="Quit",
                                command=self.handle_exit)
        quit_button.pack(side=tk.BOTTOM)
        quit_button.configure(background='yellow')
        restart_button = tk.Button(self.frame, text="Restart",
                                   command=self.restart)
        restart_button.pack(side=tk.TOP)
        restart_button.configure(background='lightgrey')

        # adding canvas widget
        self._cv = tk.Canvas(self._root, width=700, height=600)
        self._cv.pack(side=tk.LEFT)
        self._cv.configure(background='brown')
        # canvas key binding
        self._cv.bind("<Button-1>", self.handle_click)

        # adding instructions side canvas
        self.instructions = tk.Canvas(self._root, width=500, height=600)
        self.instructions.pack(side=tk.RIGHT)
        self.instructions.configure(background='lightyellow',)
        self.instructions.create_text(175, 200, fill="darkblue",
                                      font="David 14 bold",
                                text="\n Welcome!"
                                     "\n"
                                     "\n Here are the instructions:"
                                     "\n    1. choose players types:"
                                     "\n"
                                     "\n        for player1 (blue):"
                                     "\n            press '1' for human"
                                     "\n            press '2' for virtual"
                                     "\n"
                                     "\n        for player2 (red):"
                                     "\n            press '3' for human"
                                     "\n            press '4' for virtual"
                                     "\n"
                                     "\n    2. press 'Enter' to start"
                                     "\n"
                                     "\n Have fun!"
                                     "\n"
                                     "\n  * if you chose a virtual-"
                                     "\n    click anyware to begin the match"
                                     "")

    def run(self):
        """
        game will end when:
            - quit button ( or 'q') was pressed
            - a player has won
            - the board is full (tie)
        :return:
        """
        tk.mainloop()

    def show_message(self, title, msg):
        """
        show messages
        :param title:
        :param msg:
        """
        tk.messagebox.showinfo(str(title), str(msg)
                               )

    def set_start(self, event):
        """
        sets start to True, thus a loowing the game to start
        :param event:
        :return:
        """
        self.start = True
        self.show_message("start", "the game can be started!")
        for val in self.col_ind:
            val = 0

    def player1_human(self, event):
        """
        set player1 to human
        :param event:
        :return:
        """
        self.player1 = 'human'
        self.show_message("player1", "player1 is human")

    def player1_virtual(self, event):
        """
        set player1 to virtual player
        :param event:
        :return:
        """
        self.player1 = 'virtual'
        self.show_message("player1", "player1 is virtual")

    def player2_human(self, event):
        """
        set player1 to human
        :param event:
        :return:
        """
        self.player2 = 'human'
        self.show_message("player2", "player2 is human")

    def player2_virtual(self, event):
        """
        set player1 to virtual player
        :param event:
        :return:
        """
        self.player2 = 'virtual'
        self.show_message("player2", "player2 is virtual")

    def handle_click(self, event):
        """
        handles a human's turn and switches turns
        :return:
        """
        if (self.player_turn == 'blue' and self.player1 == 'human') or \
                (self.player_turn == 'red' and self.player2 == 'human'):
            column = event.x // 100
            if self.start:
                self._draw_disc(column)  # draw in lowest possible row,
                # according to column
                self.game.make_move(column)
                if self.game.get_winner():
                    self.handle_winning()
                if self.player_turn == "red":
                    self.player_turn = "blue"
                else:
                    self.player_turn = "red"
        # the next turn might be an ai's turn
        self._root.after(ms=1000, func=self.handle_virtual_player)

    def handle_virtual_player(self):
        """
        handles a virtual's turn and switches turns
        :return:
        """
        if (self.player_turn == 'blue' and self.player1 == 'virtual') or \
                (self.player_turn == 'red' and self.player2 == 'virtual'):
            # it is an ai's turn
            column = self.ai.find_legal_move()  # find a random legal column
            if self.start:
                self._draw_disc(column)  # draw in lowest possible row,
                # according to column
                self.game.make_move(column)
                if self.game.get_winner():
                    self.handle_winning()
                    # switch turns
                if self.player_turn == "red":
                    self.player_turn = "blue"
                else:
                    self.player_turn = "red"
            if (self.player_turn == 'blue' and self.player1 == 'virtual') or \
                    (self.player_turn == 'red' and self.player2 == 'virtual'):
                # the next turn is also an ai's turn
                self._root.after(ms=1000, func=self.handle_virtual_player)

    def _draw_disc(self, column):
        """
        draws a disc
        :param column:
        :return:
        """
        coordinates = DISCS_LAYOUT[column][self.col_ind[column]]
        # upper left coordinate
        x1 = coordinates[0] - 50
        y1 = coordinates[1] - 50
        # lower right coordinate
        x2 = coordinates[0] + 50
        y2 = coordinates[1] + 50
        self._cv.create_oval(x1, y1, x2, y2, width=1, fill=self.player_turn)
        # remember to later switch turns
        self.col_ind[column] += 1

    def handle_exit(self):
        """
        exits the game
        :return:
        """
        self.show_message("Exit game", "You must have something very"
                                       " important to do now.")
        self._root.quit()
        self._root.destroy()

    def handle_winning(self):
        """
        shows message accoring to end situations and offers to play another
         game
        :return:
        """
        if self.game.get_winner() == 1:
            self.show_message("c'est tout", "blue player won")
        if self.game.get_winner() == 2:
            self.show_message("c'est tout", "red player won")
        if self.game.get_winner() == 3:
            self.show_message("c'est tout", "it was a tie")
        self.show_message("play again?", "to play again press 'Restart',"
                                         " to exit press 'Quit'")
        self._cv.bind("<Button-1>", self.do_nothing)

    def do_nothing(self, event):
        """
        to unbind a button
        :param event:
        :return:
        """
        pass

    def restart(self):
        """
        restarts the game
        :return:
        """
        self._root.destroy()
        self.__init__()
        self.run()

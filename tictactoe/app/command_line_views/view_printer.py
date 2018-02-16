from textwrap import dedent
import time

from .build_a_board import BuildABoard
from .colorist import Colorist


class ViewPrinter:

    @staticmethod
    def print_intro_text():
        ViewPrinter.print_clear()
        print("Welcome!")
        print("this is tic-tac-toe!")

    @staticmethod
    def print_instructions():
        instructions = """\
            Which type of game would you like to play?
                1. Human vs. Human
                2. Human vs. Computer (you go first)
                3. Computer vs. Human (the computer goes first)
                4. Computer vs. Computer\
            """
        print("\n")
        print(dedent(instructions))

    @staticmethod
    def print_board_size():
        instructions = """\
            Which size board do you want?
                1. 3x3
                2. 4x4
            """
        print("\n")
        print(dedent(instructions))

    @staticmethod
    def print_clear():
        print(chr(27) + "[2J" + chr(27) + "[0;0H")

    @staticmethod
    def print_new_turn(board, board_decorator, last_move):
        ViewPrinter.print_clear()
        ViewPrinter.print_board(board, board_decorator, last_move)

    @staticmethod
    def print_game_over(board_decorator, players, winner=None):
        print("Okay, the game is over")
        if winner is not None: print("%s wins!" % (board_decorator.player_markers[players.index(winner)]))

    @staticmethod
    def print_error(error):
        print("\n")
        print(error)

    @staticmethod
    def print_ai_thinking():
        print("Hmmmm, the computer is thinking")

    @staticmethod
    def print_ai_update(board, board_decorator, move, turn):
        time.sleep(1)
        ViewPrinter.print_new_turn(board, board_decorator, move)
        print("It looks like, %s moved to space %s" % (board_decorator.player_markers[turn % 2], move))

    @staticmethod
    def print_humanplayer_update(board, board_decorator, move, turn):
        if move is not None:
            ViewPrinter.print_new_turn(board, board_decorator, move)
            print("Okay, %s is now on space %s" % (board_decorator.player_markers[turn % 2], move))
            time.sleep(1)
        else:
            ViewPrinter.print_new_turn(board, board_decorator, turn)

    @staticmethod
    def print_board(board, board_decorator, last_move):
        print(BuildABoard(board, board_decorator, last_move).printable_board())

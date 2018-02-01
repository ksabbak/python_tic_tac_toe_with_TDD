from textwrap import dedent
import time

def print_intro_text():
    print_clear()
    print("Welcome!")
    print("this is tic-tac-toe!")

def print_instructions():
    instructions = """\
        Which type of game would you like to play?
            1. Human vs. Human
            2. Human vs. Computer
            3. Computer vs. Computer\
        """
    print("\n")
    print(dedent(instructions))

def print_board_size():
    instructions = """\
        Which size board do you want?
            1. 3x3
            2. 4x4
        """
    print("\n")
    print(dedent(instructions))

def print_who_first(player_first):
    print("\n")
    if player_first:
        print("Great, you'll go first!")
    else:
        print("Cool! The computer will go first.")

def print_clear():
    print(chr(27) + "[2J" + chr(27) + "[0;0H")

def print_new_turn(board, last_move, player_one, player_two):
    print_clear()
    _print_board(board, last_move, player_one, player_two)

def print_game_over(winner=None):
    print("Okay, the game is over")
    if winner is not None: print("%s wins!" % _color_text(winner.marker, winner.color))

def print_ai_thinking():
    print("Hmmmm, the computer is thinking")

def print_ai_update(game, move):
    time.sleep(1)
    print_new_turn(game.board, game.last_move, *game.players)
    print("It looks like, %s moved to space %s" % (_color_text(game.current_player.marker, game.current_player.color), move))

def print_humanplayer_update(board, aesthetics, move, turn):
    if move is not None:
        print_new_turn(board, move, aesthetics)
        print("Okay, %s is now on space %s" % (aesthetics.markers[turn % 2], move))
        time.sleep(1)
    else:
        print_new_turn(board, aesthetics, turn)

#BAD INPUT PRINT
def print_sorry(about=None):
    if about == "game type":
        print("Please enter the numeral 1, 2, or 3:")
    elif about == "board type":
        print("Please enter the numeral 1, or 2:")
    elif about == "marker length":
        print("Sorry, your marker can only be one character.")
    elif about == "no coord":
        print("Sorry, I can't find that coordinate.")
    elif about == "taken":
        print("Sorry, looks like that spot is taken.")
    elif about == "match marker":
        print("Each marker needs to be different, let's try again.")
    elif about == "color":
        print("I didn't quite understand that. Try one of these: ")
        print(_color_option_string())
        print("or 'none' for default")
    else:
        print("Sorry, that won't work, please try again.")


def _print_board(board, player_one, player_two, last_move):
    board_str = _build_board(self.board, self.color_spaces)
    print(BuildABoard(board, player_one, player_two, last_move).printable_board())

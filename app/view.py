from copy import copy
from textwrap import dedent
import time

def print_intro_text():
    print("Welcome!")
    print("this is tic-tac-toe!")

def print_instructions():
    instructions = """\
        Which type of game would you like to play?
            1. Human vs. Human
            2. Human vs. Computer
            3. Computer vs. Computer\
        """
    print(dedent(instructions))

def print_board_size():
    instructions = """\
        Which size board do you want?
            1. 3x3
            2. 4x4
        """
    print(dedent(instructions))

def print_who_first(player_first):
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

def print_ai_update(game, move):
    time.sleep(0.5)
    print("Hmmmm, the computer is thinking")
    time.sleep(1)
    print_new_turn(game.board, game.last_move, *game.players)
    print("It looks like, %s moved to space %s" % (_color_text(game.current_player.marker, game.current_player.color), move))

def print_humanplayer_update(game, move):
    if move is not None:
        print_new_turn(game.board, game.last_move, *game.players)
        print("Okay, %s is now on space %s" % (_color_text(game.current_player.marker, game.current_player.color), move))
        time.sleep(1)
    else:
        print_new_turn(game.board, game.last_move, *game.players)

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

def _print_board(board, last_move, player_one, player_two, ):
    color_spaces = _color_spaces(board, player_one, player_two, last_move)
    board_str = _build_board(board, color_spaces)
    print(board_str)

#GETTERS: 
def get_game_type_input():
    print("Please enter the number of your selection:")
    return input().strip()

def get_marker(player):
    print("Please enter the marker choice for %s." % player)
    return input().strip()

def get_color(thing_to_color):
    print("What color would you like %s to be?" % thing_to_color)
    return input().strip()
        
def get_player_move(marker, color):
    print("Where would you like to move, Player %s?" % _color_text(marker, color))
    move = input().strip()
    return move

def get_who_first():
    print("Great, would you like to move first?")
    return input().strip()

# COLORS: 
def colors():
    colors = {  
                "BLACK" : "\033[1;30m",
                "RED" : "\033[1;31m",
                "GREEN" : "\033[0;32m",
                "YELLOW" : "\033[1;33m",
                "BLUE" : "\033[1;34m",
                "PINK" : "\033[1;35m",
                "CYAN"  : "\033[1;36m",
                "WHITE": "\033[1;37m"
             }
    return colors

def _color_option_string():
    color_string = ""
    for text, color in colors().items():
        color_string += _color_text(text, color) + "\n"
    return color_string

def _color_text(text, color):
    color = _assign_color_value(color)
    no_color = "\033[0m"
    return (color + text + no_color)

def _uncolor_text(text, color):
    color = _assign_color_value(color)
    no_color = "\033[0m"
    return no_color + text + color

def _assign_color_value(color):
    if color.upper() in colors().keys(): 
        color = colors()[color.upper()]
    elif color == "none":
        color = ""
    return color


# BUILD BOARD + HELPER METHODS:
def _build_board(board, color_spaces):
        first_row = _color_text(_build_first_row(board.side_length), board.color)
        filler_row = _color_text(_build_filler_row(board.side_length), board.color)
        board_str = first_row
        for space in range(0, len(board.spaces)):
            if space % board.side_length == 0:
                board_str += _color_text(board.coordinates[space][0], board.color) + " "
            board_str += " " + color_spaces[space] +  _color_text(" |", board.color)
            if (space % board.side_length == board.side_length - 1
                 and space != len(board.spaces) -1 ):
                board_str = board_str[:-5] + "\033[0m"
                board_str += "\n" + filler_row
        return board_str[:-5] + "\033[0m" + "\n"
        
def _color_spaces(board, player_one, player_two, last_move):
    spaces = copy(board.spaces)
    new_spaces = []
    for i, space in enumerate(spaces):
        if space == player_one.marker:
            new_space = _color_text(space, player_one.color)
        elif space == player_two.marker:
            new_space = _color_text(space, player_two.color)
        else:
            new_space = space

        if i == last_move:
            new_space = _color_text(new_space, "\033[;4m")

        new_spaces.append(new_space)
    return new_spaces

def _build_first_row(side_length):
    first_row = ""
    for num in range(1, side_length + 1):
        first_row += "   " + str(num)
    first_row += "\n" 
    return first_row

def _build_filler_row(side_length):
    filler_row = "  ==="
    for row in range(1, side_length):
        filler_row += "+==="
    filler_row += "\n" 
    return filler_row


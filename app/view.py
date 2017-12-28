from textwrap import dedent
import time

# from .board import Board

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

def get_game_type_input():
    print("Please enter the number of your selection:")
    return input().strip()

def get_marker(player):
    print("Please enter the marker choice for %s." % player)
    return input().strip()

def print_sorry(about=None):
    if about == "game type":
        print("Please enter the numeral 1, 2, or 3:")
    elif about == "marker length":
        print("Sorry, your marker can only be one character.")
    elif about == "no coord":
        print("Sorry, I can't find that coordinate.")
    elif about == "taken":
        print("Sorry, looks like that spot is taken.")
    elif about == "match marker":
        print("Each marker needs to be different, let's try again.")
    else:
        print("Sorry, that won't work, please try again.")

def get_who_first():
    print("Great, would you like to move first?")
    return input().strip()

def print_who_first(player_first):
    if player_first:
        print("Great, you'll go first!")
    else:
        print("Cool! The computer will go first.")

def print_clear():
    print(chr(27) + "[2J" + chr(27) + "[0;0H")

def print_board(board):
    print(str(board))

def print_new_turn(board):
    print_clear()
    print_board(board)
    
def get_player_move(marker):
    print("Where would you like to move, Player %s?" % marker)
    move = input().strip()
    return move

def print_game_over(winner=None):
    print("Okay, the game is over")
    if winner is not None: print("%s wins!" % winner.marker)

def print_ai_update(board, computer_marker, move):
    time.sleep(0.5)
    print("Hmmmm, the computer is thinking")
    time.sleep(1)
    print_new_turn(board)
    print("It looks like, %s moved to space %s" % (computer_marker, move))

def print_humanplayer_update(board, human_marker, move):
    if move is not None:
        print_new_turn(board)
        print("Okay, %s is now on space %s" % (human_marker, move))
        time.sleep(1)
    else:
        print_new_turn(board)

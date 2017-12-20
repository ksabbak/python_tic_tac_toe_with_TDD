from textwrap import dedent

# from .board import Board

def print_intro_text():
    print("Welcome!")
    print("this is tic-tac-toe!")

def print_instructions():
    instructions = """\
        Which type of game would you like to play?
            1. Human vs. Human
            2. Human vs. Computer
            3. Computer vs. Computer
        Please enter the number of your selection:\
        """
    print(dedent(instructions))

def print_who_first():
    print("Great, would you like to move first?")

def print_clear():
    print(chr(27) + "[2J" + chr(27) + "[0;0H")

def print_board(board):
    print(board.to_str())

def print_new_turn(board):
    print_clear()
    print_board(board)
    
def print_get_player_move(marker):
    print("Where would you like to move, Player %s" % marker)
    move = input()
    return move

def print_game_over(winner=None):
    print("Okay, the game is over")
    if winner is not None: print("%s wins!" % winner)

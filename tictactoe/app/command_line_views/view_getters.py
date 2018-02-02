def get_game_type_input():
    print("\n")
    print("Please enter the number of your selection:")
    return input().strip()

def get_marker(player):
    print("\n")
    print("Please enter the marker choice for %s." % player)
    return input().strip()

def get_color(thing_to_color):
    print("\n")
    print("What color would you like %s to be? (enter 'help' for options)" % thing_to_color)
    return input().strip()

def get_player_move(marker):
    print("\n")
    print("Where would you like to move, Player %s?" % marker)
    move = input().strip()
    return move

def get_who_first():
    print("\n")
    print("Great, would you like to move first?")
    return input().strip()


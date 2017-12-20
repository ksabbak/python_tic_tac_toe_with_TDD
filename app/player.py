from .view import print_get_player_move

class Player:
    def __init__(self, marker):
        self.marker = marker

    def get_move(self, board=None):
        move = print_get_player_move(self.marker)
        return int(move)

class HumanPlayer(Player):
    pass

from .view import print_get_player_move, print_human_update

class Player:
    def __init__(self, marker):
        self.marker = marker

    def get_move(self, board=None):
        move = print_get_player_move(self.marker)
        return int(move)

class HumanPlayer(Player):
    def print_update(self, board, move):
        print_human_update(board, self.marker, move)

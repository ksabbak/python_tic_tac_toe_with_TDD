from .view import print_human_update

class Player:
    def __init__(self, marker):
        self.marker = marker

    def make_move(self, board, move):
        board.mark_space(move, self.marker)


class HumanPlayer(Player):

    # def get_move(self, board=None):
    #     move = print_get_player_move(self.marker)
    #     return int(move)

    def print_update(self, board, move):
        print_human_update(board, self.marker, move)

    def is_ai(self):
        return False


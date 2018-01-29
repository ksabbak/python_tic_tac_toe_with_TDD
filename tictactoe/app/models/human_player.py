from .player import Player


class HumanPlayer(Player):

    def make_move(self, board, move):
        move = int(move)
        return super().make_move(board, move)

    def is_ai(self):
        return False

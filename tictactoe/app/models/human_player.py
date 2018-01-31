from .player import Player


class HumanPlayer(Player):

    def make_move(self, board, move, turn):
        move = int(move)
        return super().make_move(board, move, turn)

    def is_ai(self):
        return False

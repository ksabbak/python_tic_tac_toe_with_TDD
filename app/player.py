class Player:
    def __init__(self, marker):
        self.marker = marker
        self.moves = []

    def make_move(self, board, move):
        board.mark_space(move, self.marker)
        return move


class HumanPlayer(Player):

    def make_move(self, board, move):
        move = int(move)
        return super().make_move(board, move)

    def is_ai(self):
        return False


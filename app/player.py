class Player:
    def __init__(self, marker):
        self.marker = marker
        self.moves = []

    def make_move(self, board, move):
        board.mark_space(move, self.marker)
        self.moves.append(move)
        return move

    def undo(self):
        if self.moves:
            return self.moves.pop()

class HumanPlayer(Player):

    def make_move(self, board, move):
        move = int(move)
        return super().make_move(board, move)

    def is_ai(self):
        return False


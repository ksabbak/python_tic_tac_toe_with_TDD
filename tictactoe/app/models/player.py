class Player:
    def __init__(self, marker, color=""):
        self.color = color
        self.marker = marker
        self.moves = []

    def last_move(self):
        if self.moves: return self.moves[-1]

    def make_move(self, board, move):
        board.mark_space(move, self.marker)
        self.moves.append(move)
        return move

    def undo(self):
        if self.moves:
            return self.moves.pop()




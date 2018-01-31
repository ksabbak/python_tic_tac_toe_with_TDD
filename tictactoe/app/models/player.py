class Player:
    def __init__(self):
        self.moves = []

    def last_move(self):
        if self.moves: return self.moves[-1]

    def make_move(self, board, move, turn):
        board.mark_space(move, turn)
        self.moves.append(move)
        return move

    def undo(self):
        if self.moves:
            return self.moves.pop()




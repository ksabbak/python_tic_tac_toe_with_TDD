class Player:
    def make_move(self, board, move, turn):
        board.mark_space(move, turn)
        return move





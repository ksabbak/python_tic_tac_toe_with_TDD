class Player:
    def __init__(self, turn_order):
        self.turn_order = turn_order

    def make_move(self, board, move, turn):
        board.mark_space(move, turn)
        return move





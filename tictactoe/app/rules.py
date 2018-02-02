from .win_conditions import all_win_conditions


class Rules:
    def __init__(self, board):
        self.board = board
        self.all_win_conditions = self._set_win_conditions()

    def winning_marker(self, board=None):
        if board is None:
            board = self.board
        for win_condition in self.all_win_conditions:
            board_sample = list(map(lambda x: board.spaces[x], win_condition))
            if ((" " not in board_sample)
               and len(set(map(lambda x: x % 2, board_sample))) == 1):
                return board_sample[0] % 2

    def _set_win_conditions(self):
        self.all_win_conditions = None
        return all_win_conditions(self.board)


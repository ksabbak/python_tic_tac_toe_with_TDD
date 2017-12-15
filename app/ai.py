from random import randint
from copy import copy

from .player import Player
from .board import Board
from .win_conditions import winner

class AI(Player):
    
    def get_move(self, board):
        move = self._get_winning_move(board) 
        move = move or self._stop_immidate_loss(board) 
        move = move or self._make_good_choice(board) 
        move = move or 0
        return move

    def _get_winning_move(self, board):
        return self._make_immediate_vital_move(board, self.marker)

    def _stop_immidate_loss(self, board):
        opponent_marker = self._deduce_opponent_marker(board)
        return self._make_immediate_vital_move(board, opponent_marker)

    def _deduce_opponent_marker(self, board):
        for space in range(0, len(board.spaces)):
            if (not board.space_is_empty(space) 
                and (board.spaces[space] != self.marker)):
                return board.spaces[space]

    def _make_immediate_vital_move(self, board, marker):
        for space in board.empty_spaces():
            copy_board = copy(board)
            copy_board.mark_space(space, marker)
            if winner(copy_board) == marker: return space

    def _make_good_choice(self, board):
        if ((len(board.empty_spaces()) == len(board.spaces) - 1) 
            and board.space_is_empty(4)):
            return 4

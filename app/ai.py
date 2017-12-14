from random import randint
from copy import copy

from .player import Player
from .board import Board
from .win_conditions import winner

class AI(Player):
    
    def get_move(self, board):
        move = self._get_winning_move(board) or self._stop_immidate_loss(board) or 0
        return move

    def _get_winning_move(self, board):
        for space in range(0, len(board.spaces)):
            copy_board = copy(board)
            copy_board.mark_space(space, self.marker)
            if winner(copy_board) == self.marker: return space

    def _stop_immidate_loss(self, board):
        opponent_marker = self._deduce_opponent_marker(board)
        for space in range(0, len(board.spaces)):
            copy_board = copy(board)
            copy_board.mark_space(space, opponent_marker)
            if winner(copy_board) == opponent_marker: return space

    def _deduce_opponent_marker(self, board):
        for space in range(0, len(board.spaces)):
            if (not board.space_is_empty(space) 
                and (board.spaces[space] != self.marker)):
                return board.spaces[space]

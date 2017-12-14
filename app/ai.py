from random import randint
from copy import copy

from .player import Player
from .board import Board
from .win_conditions import winner

class AI(Player):
    
    def get_move(self, board):
        move = self.get_winning_move(board) or 0
        return move

    def get_winning_move(self, board):
        for space in range(0, len(board.spaces)):
            copy_board = copy(board)
            copy_board.mark_space(space, self.marker)
            if winner(copy_board) == self.marker: return space




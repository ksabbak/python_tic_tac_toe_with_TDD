from random import randint, choice
from copy import copy
from math import factorial

from .player import Player
from .board import Board
from tictactoe.app.move_logic import MoveLogic

class AI(Player):
    def __init__(self, marker, color=""):
        super().__init__(marker, color)

    def make_move(self, board, move=None):
        move = self._get_move(board)
        return super().make_move(board, move)

    def is_ai(self):
        return True

    def _get_move(self, board):
        move_logic = MoveLogic(self.marker, board)
        return move_logic.get_move()



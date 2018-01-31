from random import randint, choice
from copy import copy
from math import factorial

from .player import Player
from .board import Board
from tictactoe.app.move_logic import MoveLogic

class AI(Player):
    def make_move(self, board, move, turn):
        move = self._get_move(board, turn)
        return super().make_move(board, move, turn)

    def is_ai(self):
        return True

    def _get_move(self, board, turn):
        move_logic = MoveLogic(board)
        return move_logic.get_move(turn)



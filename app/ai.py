from random import randint

from .player import Player
from .board import Board
from .win_conditions import winner

class AI(Player):
    
    def get_move(self, board):
        return 0

    def get_winning_move(self, board):
        pass



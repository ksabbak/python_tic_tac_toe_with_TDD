from random import randint

from .player import Player
from .board import Board

class AI(Player):
    
    def get_move(self, board):
        return randint(0,8)

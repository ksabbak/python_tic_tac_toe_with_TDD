from random import randint

from .player import Player
from .board import Board

class AI(Player):
    
    def get_move(self, board):
        while True:
            move = randint(0,8) 
            if board.space_is_empty(move): return move

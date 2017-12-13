import sys


from .board import Board
from .player import Player

class Game:
    def __init__(self, player1="x", player2="o"):
        self.board = Board()
        self.players = [Player(player1), Player(player2)]

    def is_over(self):
        winner = (self.board.spaces[0] == self.board.spaces[1] and self.board.spaces[0] == self.board.spaces[2]) 
        winner = winner or (self.board.spaces[3] == self.board.spaces[4] and self.board.spaces[3] == self.board.spaces[5]) 
        return self.board.is_full() or winner

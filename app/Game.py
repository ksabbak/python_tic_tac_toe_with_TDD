import sys


from .board import Board
from .player import Player

class Game:
   def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]

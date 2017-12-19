import sys

from .board import Board
from .player import Player
from .end_conditions import winner, is_over

class Game:
    def __init__(self, player1=Player("x"), player2=Player("o")):
        self.board = Board()
        self.players = [player1, player2]

    def play(self):
        print("Welcome!")
        print("this is tic-tac-toe!")
        i = 0
        while not is_over(board):
            current_player = self.players[i%2]
            move = current_player.get_move()
            self.board.mark_space(move, current_player.marker)
            print(self.board.to_str())
            i += 1
        print("Okay, the game is over")
        if winner(self.board): print("%s wins!" % winner(self.board))





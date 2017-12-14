import sys

from .board import Board
from .player import Player
from .win_conditions import winner

class Game:
    def __init__(self, player1="x", player2="o"):
        self.board = Board()
        self.players = [Player(player1), Player(player2)]

    def play(self):
        print("Welcome!")
        print("this is tic-tac-toe!")
        i = 0
        while not self.is_over():
            current_player = self.players[i%2]
            move = current_player.get_move()
            self.board.mark_space(move, current_player.marker)
            print(self.board.to_str())
            i += 1
        print("Okay, the game is over")
        if winner(self.board): print("%s wins!" % winner(self.board))

    def is_over(self):
        return not not (self.board.is_full() or winner(self.board))



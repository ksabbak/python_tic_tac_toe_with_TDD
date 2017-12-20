import sys
import time

from .board import Board
from .player import Player, HumanPlayer
from .end_conditions import winner, is_over
from .view import print_new_turn, print_game_over

class Game:
    def __init__(self, player1=HumanPlayer("x"), player2=HumanPlayer("o")):
        self.board = Board()
        self.players = [player1, player2]

    def play(self):
        i = 0
        while not is_over(self.board):
            time.sleep(1)
            print_new_turn(self.board)
            current_player = self.players[i%2]
            move = current_player.get_move(self.board)
            print("Okay, %s is now on space %s" % (current_player.marker, move))
            self.board.mark_space(move, current_player.marker)
            print(self.board.to_str())
            i += 1
        print_game_over(winner(self.board))

    @classmethod
    def pvp(cls):
        return Game()

    @classmethod
    def mixed_game(cls, order):
        return Game(**order)

    @classmethod
    def cvc(cls):
        return Game(AI("X"), AI("O"))

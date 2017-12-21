import sys

from .board import Board
from .player import HumanPlayer
from .end_conditions import winner, is_over
from .view import print_new_turn, print_game_over, print_computer_update

class Game:
    def __init__(self, player1=HumanPlayer("x"), player2=HumanPlayer("o")):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = 0
        self._get_current_player()
    
    def play(self):
        print_new_turn(self.board)
        while not is_over(self.board):
            self._take_a_turn()
        print_game_over(winner(self.board))

    def is_over(self):
        return is_over(self.board)

    def take_a_turn(self):
        self._get_current_player()
        move = self.current_player.get_move(self.board)
        self.board.mark_space(move, self.current_player.marker)
        self.turn += 1
        return move

    def winner(self):
        return winner(self.board)

#PRIVATE METHODS

    def _get_current_player(self):
        self.current_player = self.players[self.turn % 2]

#CLASS METHODS: 
    @classmethod
    def pvp(cls):
        return Game()

    @classmethod
    def mixed_game(cls, order):
        return Game(**order)

    @classmethod
    def cvc(cls):
        return Game(AI("X"), AI("O"))

import sys

from .board import Board
from .player import HumanPlayer
from .end_conditions import winner, is_over
from .view import print_new_turn, print_game_over, print_computer_update

class Game:
    def __init__(self, player1=HumanPlayer("x"), player2=HumanPlayer("o")):
        self.board = Board()
        self.players = [player1, player2]

    @classmethod
    def pvp(cls):
        return Game()

    @classmethod
    def mixed_game(cls, order):
        return Game(**order)

    @classmethod
    def cvc(cls):
        return Game(AI("X"), AI("O"))

    def play(self):
        turn = 0
        print_new_turn(self.board)
        while not is_over(self.board):
            current_player = self._get_current_player(turn)
            move = current_player.get_move(self.board)
            self.board.mark_space(move, current_player.marker)
            current_player.print_update(self.board, move)
            turn += 1
        print_game_over(winner(self.board))

    def _player_is_AI(self, player):
        return player.__class__.__name__ == "AI"

    def _get_current_player(self, turn):
        return self.players[turn%2]

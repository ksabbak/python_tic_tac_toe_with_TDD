from .ai import AI
from .board import Board
from .end_conditions import winning_marker
from .player import HumanPlayer


class Game:
    def __init__(self, player1=HumanPlayer("x"), player2=HumanPlayer("o")):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = 0
        self._get_current_player()

    def is_over(self):
        return (self.board.is_full() or winning_marker(self.board))

    def start_turn(self, move=None):
        move = self.current_player.make_move(self.board, move)
        return move

    def end_turn(self):
        self.turn += 1
        self._get_current_player()

    def winner(self):
        for player in self.players:
            if winning_marker(self.board) == player.marker: return player

    def undo_turn(self):
        for player in self.players:
            move = player.undo()
        self.turn -= 1

# PRIVATE METHODS

    def _get_current_player(self):
        self.current_player = self.players[self.turn % 2]

# CLASS METHODS:
    @classmethod
    def pvp(cls):
        return Game()

    @classmethod
    def mixed_game(cls, order):
        return Game(**order)

    @classmethod
    def cvc(cls):
        return Game(AI("X"), AI("O"))

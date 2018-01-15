from .ai import AI
from .board import Board
from .player import HumanPlayer


class Game:
    def __init__(self, player1=HumanPlayer("x"), player2=HumanPlayer("o"), board=9, board_color=""):
        self.board = Board.create_from_scratch(board, board_color)
        self.players = [player1, player2]
        self.turn = 0
        self._get_current_player()
        self.last_move = None

    def is_over(self):
        return (self.board.is_full() or self.board.winning_marker())

    def start_turn(self, move=None):
        move = self.current_player.make_move(self.board, move)
        self.last_move = self.current_player.last_move()
        return move

    def end_turn(self):
        self.turn += 1
        self._get_current_player()

    def winner(self):
        for player in self.players:
            if self.board.winning_marker() == player.marker: return player

    def undo_turn(self):
        for player in self.players:
            move = player.undo()
            if move is not None: self.board.clear_space(move)
        self.turn -= 1

# PRIVATE METHODS

    def _get_current_player(self):
        self.current_player = self.players[self.turn % 2]

# CLASS METHODS:
    @classmethod
    def pvp(cls, player1, player2, board, board_color):
        return Game(HumanPlayer(*player1), HumanPlayer(*player2), board, board_color)

    @classmethod
    def cvp(cls, player1, player2, board, board_color):
        return Game(AI(*player1), HumanPlayer(*player2), board, board_color)

    @classmethod
    def pvc(cls, player1, player2, board, board_color):
        return Game(HumanPlayer(*player1), AI(*player2), board, board_color)

    @classmethod
    def cvc(cls, player1, player2, board, board_color):
        return Game(AI(*player1), AI(*player2), board, board_color)

from .ai import AI
from .board import Board
from .human_player import HumanPlayer
from ..rules import Rules


class Game:
    def __init__(self, player1=HumanPlayer("x"), player2=HumanPlayer("o"), board=9):
        self.board = Board.create_fresh_board(board)
        self.players = [player1, player2]
        self.turn = 0
        self._get_current_player()
        self.last_move = None

    def is_over(self):
        return (self.board.is_full() or self.rules.winning_marker())

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
        self._get_current_player()
        self.last_move = self.current_player.last_move()


    def _get_current_player(self):
        self.current_player = self.players[self.turn % 2]


    @classmethod
    def pvp(cls, player1, player2, board):
        return Game(HumanPlayer(*player1), HumanPlayer(*player2), board)

    @classmethod
    def cvp(cls, player1, player2, board):
        return Game(AI(*player1), HumanPlayer(*player2), board)

    @classmethod
    def pvc(cls, player1, player2, board):
        return Game(HumanPlayer(*player1), AI(*player2), board)

    @classmethod
    def cvc(cls, player1, player2, board):
        return Game(AI(*player1), AI(*player2), board)

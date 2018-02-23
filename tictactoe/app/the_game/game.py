from .ai import AI
from .board import Board
from .human_player import HumanPlayer
from .rules import Rules


class Game:
    def __init__(self, moves, player1=HumanPlayer(0), player2=HumanPlayer(1), board=9):
        self.board = Board.create_fresh_board(board)
        self.players = [player1, player2]
        self.turn = 0
        self._get_current_player()
        self.last_move = None
        self.rules = Rules(self.board)
        self._rebuild_game(moves)

    def is_over(self):
        return (self.board.is_full() or self.rules.winning_marker() is not None)

    def start_turn(self, move=None):
        move = self.current_player.make_move(self.board, move, self.turn)
        self.last_move = self._get_last_move()
        return move

    def end_turn(self):
        self.turn += 1
        self._get_current_player()

    def winner(self):
        for player in range(0, len(self.players)):
            if self.rules.winning_marker() == player: return self.players[player]

    def undo_turn(self):
        self.turn -= 1
        for player in self.players:
            move = self._get_last_move()
            if move is not None:
                self.turn -= 1
                self.board.clear_space(move)
        self._get_current_player()
        self.last_move = self._get_last_move()


    def _get_current_player(self):
        self.current_player = self.players[self.turn % len(self.players)]

    def _get_last_move(self):
        if self.turn in self.board.spaces:
            return self.board.spaces.index(self.turn)



    @classmethod
    def pvp(cls, board, moves=[]):
        game = Game(moves, HumanPlayer(0), HumanPlayer(1), board)
        return game

    @classmethod
    def cvp(cls, board, moves=[]):
        game = Game(moves, AI(0), HumanPlayer(1), board)
        return game

    @classmethod
    def pvc(cls, board, moves=[]):
        game = Game(moves, HumanPlayer(0), AI(1), board)
        return game

    @classmethod
    def cvc(cls, board, moves=[]):
        game = Game(moves, AI(0), AI(1), board)
        return game

    def _rebuild_game(self, moves):
        for index, move in enumerate(moves):
            if move != " ":
                self.board.mark_space(index, int(move))
                self.end_turn()


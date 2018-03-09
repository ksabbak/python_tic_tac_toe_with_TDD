from random import choice
from copy import copy
from math import factorial, inf

from .rules import Rules

class MoveLogic:
    def __init__(self, board):
        self.board = board
        self.rules = Rules(self.board)


    def get_move(self, turn):
        self.turn = turn
        return self._minimax(turn, self.board)

    def _minimax(self, turn, board):
        moves = {}
        for space in board.empty_spaces():
            new_board = copy(board)
            new_board.mark_space(space, turn)
            move_score = self._calculate_move_score(new_board, turn)
            if move_score is not None:
                moves[space] = move_score
            else:
                moves[space] = self._minimax(turn + 1, new_board)

        return self._choose_best(moves, turn)

    def _calculate_move_score(self, board, turn):
        if board.is_full() or self._max_calculated_turns(turn):
            return 0
        elif self.rules.winning_marker(board) is not None:
            return self._player_weights(turn)

    def _max_calculated_turns(self, turn):
        return (turn - self.turn) > self.board.side_length()

    def _turn_matches_player(self, turn):
        return self._player_turn(turn) == self._player_turn(self.turn)

    def _player_weights(self, turn):
        turn_weight = len(self.board.spaces) - turn
        return turn_weight if self._turn_matches_player(turn) else -turn_weight

    def _choose_best(self, moves, turn):
        if turn == self.turn:
            return self._choose_best_move(moves, turn)
        else:
            return self._choose_best_value(moves, turn)

    def _choose_best_value(self, moves, turn):
        best_value = self._player_weights(turn) * -inf
        for space, value in moves.items():
            if ((self._turn_matches_player(turn) and value > best_value)
                or
                (not self._turn_matches_player(turn) and (value < best_value))):
                best_value = value
        return best_value

    def _choose_best_move(self, moves, turn):
        options = []
        best_value = self._choose_best_value(moves, turn)
        for space, value in moves.items():
            if value == best_value:
                options.append(space)
        return choice(options)

    def _player_turn(self, turn):
        return turn % 2

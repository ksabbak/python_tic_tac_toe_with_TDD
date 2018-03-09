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

    def _minimax(self, turn, board, alpha=-inf, beta=inf):
        moves = {}
        if beta >= alpha:
            for space in board.empty_spaces():
                new_board = copy(board)
                new_board.mark_space(space, turn)
                move_score = self._calculate_move_score(new_board, turn)
                if move_score is not None:
                    moves[space] = move_score
                else:
                    moves[space] = self._minimax(turn + 1, new_board, alpha, beta)
                    alpha = self._set_alpha(turn, alpha, moves[space])
                    beta = self._set_beta(turn, beta, moves[space])
            return self._choose_best(moves, turn)
        else:
            return self._alpha_or_beta(turn, alpha, beta)

    def _alpha_or_beta(self, turn, alpha, beta):
        if self._turn_matches_player(turn):
            return alpha
        else:
            return beta

    def _set_alpha(self, turn, alpha, score):
        if self._turn_matches_player(turn):
            alpha = max(alpha, score)
        return alpha

    def _set_beta(self, turn, beta, score):
        if not self._turn_matches_player(turn):
            beta = min(beta, score)
        return beta

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
        best_value = max(list(moves.values()))
        for space, value in moves.items():
            best_value = max(value, best_value)
            if value == best_value:
                options.append(space)
        return choice(options)

    def _player_turn(self, turn):
        return turn % 2


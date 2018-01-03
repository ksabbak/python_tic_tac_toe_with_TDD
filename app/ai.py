from random import randint, choice
from copy import copy
from math import factorial

from .player import Player
from .board import Board

class AI(Player):
    def __init__(self, marker, color=""):
        super().__init__(marker, color)
        self.transposition_table = {}

    def make_move(self, board, move):
        move = self._get_move(board)
        return super().make_move(board, move)

    def is_ai(self):
        return True

    # PRIVATE METHODS

    # MOVE LOGIC
    def _get_move(self, board):
        self.opponent_marker = self._deduce_opponent_marker(board) 
        self.move_weights = {}
        self._get_move_weights(board)
        return self._pick_the_best_move(board)

    def _pick_the_best_move(self, board):
        best_spaces = []
        most_weight = -factorial(len(board.spaces))
        for space, weight in self.move_weights.items():
            if most_weight == weight:
                best_spaces.append(space)
            elif most_weight < weight:
                most_weight = weight 
                best_spaces = [space]
        if best_spaces:
            return choice(best_spaces)

    def _get_move_weights(self, board):
        for space in board.empty_spaces():
            board2 = copy(board)
            self.move_weights[space] = self._weigh_move(board2, space)

    def _weigh_move(self, board, set_move=None, turn="self", depth=0):
        if board.is_full() or depth > board.side_length + 1: return 0
        if set_move is not None:
            board.mark_space(set_move, self.marker)
            if str(board.spaces) in self.transposition_table.keys():
                weight = self.transposition_table[str(board.spaces)]
            if board.winning_marker(): return factorial(len(board.spaces))
            if self._check_move_for_win(board, self.opponent_marker) is not None: return -factorial(len(board.spaces))
            turn = "other"
        weight = 0
        for move in board.empty_spaces():
            boardcopy = copy(board)
            value = 1 if turn == "self" else -1
            weight += self._calculate_move(boardcopy, move, value, depth)
        self._transpose(board, weight)
        return weight

    def _calculate_move(self, board, move, win_weight, depth):
        marker = self.marker if win_weight > 0 else self.opponent_marker
        if self._check_move_for_win(board, marker) is not None:
            weight = win_weight
        else:
            board.mark_space(move, marker)
            if str(board.spaces) in self.transposition_table.keys():
                weight = self.transposition_table[str(board.spaces)]
            else:
                depth +=1
                next_turn = "self" if win_weight < 0 else "other"
                weight = self._weigh_move(board, turn=next_turn, depth=depth)
                self._transpose(board, weight)
        return weight

    def _check_move_for_win(self, board, marker):
        for space in board.empty_spaces():
            copy_board = copy(board)
            copy_board.mark_space(space, marker)
            if copy_board.winning_marker() == marker: return space

    # MECHANICS
    def _deduce_opponent_marker(self, board):
        for space in range(0, len(board.spaces)):
            if (not board.space_is_empty(space) 
                and (board.spaces[space] != self.marker)):
                return board.spaces[space]
        return chr(ord(self.marker.strip('\033[0m')) + 1)

    def _transpose(self, board, value):
        if str(board.spaces) not in self.transposition_table.keys():
            self.transposition_table[str(board.spaces)] = value

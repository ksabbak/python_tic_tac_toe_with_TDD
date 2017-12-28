from random import randint, choice
from copy import copy

from .player import Player
from .board import Board
from .end_conditions import winning_marker

class AI(Player):
    
    def make_move(self, board, move):
        move = self._get_move(board)
        return super().make_move(board, move)

    def is_ai(self):
        return True

    # PRIVATE METHODS

    # MOVE LOGIC
    def _get_move(self, board):
        self.opponent_marker = self._deduce_opponent_marker(board) or chr(ord(self.marker) + 1)
        self.move_weights = {}
        self._get_move_weights(board)
        return self._pick_the_best_move()

    def _pick_the_best_move(self):
        print(self.move_weights)
        best_spaces = []
        most_weight = -1000000000
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
            self.move_weights[space] = sum(self._weigh_move_with_array(board2, space, array=[]))

    def _weigh_move(self, board, set_move=None, turn="self"):
        if board.is_full(): return 0
        board2 = copy(board)
        if set_move is not None:
            board2.mark_space(set_move, self.marker)
            if winning_marker(board2): return 100000000000
            if self._check_move_for_win(board2, self.opponent_marker) is not None: return -10000000000
            turn = "other"
        weight = 0
        for move in board2.empty_spaces():
            boardcopy = copy(board2)
            if turn == "self":
                weight += self._calculate_move(boardcopy, move, self.marker, 10)
            else:
                weight += self._calculate_move(boardcopy, move, self.opponent_marker, -10)
        return weight

    def _weigh_move_with_array(self, board, set_move=None, turn="self", array=[]):
        if board.is_full(): return
        if set_move is not None:
            board.mark_space(set_move, self.marker)
            if board.winning_marker(): return [100000000000]
            if self._check_move_for_win(board, self.opponent_marker) is not None: return [-10000000000]
            turn = "other"
        for move in board.empty_spaces():
            boardcopy = copy(board)
            if turn == "self":
                self._calculate_move(boardcopy, move, self.marker, 10, array)
            else:
                self._calculate_move(boardcopy, move, self.opponent_marker, -10, array)
        return array


    def _calculate_move(self, board, move, marker, win_weight, array):
        if self._check_move_for_win(board, marker) is not None:
            array += [win_weight]
        else:
            board.mark_space(move, marker)
            next_turn = "self" if win_weight < 0 else "other"
            self._weigh_move_with_array(board, turn=next_turn, array=array)

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

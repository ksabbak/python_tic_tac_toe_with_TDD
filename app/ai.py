from random import randint, choice
from copy import copy
import pdb

from .player import Player
from .board import Board
from .end_conditions import winner, is_over

class AI(Player):
    
    def get_move(self, board):
        self.opponent_marker = self._deduce_opponent_marker(board) or chr(ord(self.marker) + 1)
        # self.move_weights = {}
        # self._get_move_weights(board)
        return self._make_best_choice(board)


    def _get_winning_move(self, board):
        return self._make_immediate_vital_move(board, self.marker)

    def _stop_immidate_loss(self, board):
        return self._make_immediate_vital_move(board, self.opponent_marker)

    def _make_immediate_vital_move(self, board, marker):
        for space in board.empty_spaces():
            copy_board = copy(board)
            copy_board.mark_space(space, marker)
            if winner(copy_board) == marker: return space

    def _make_good_choice(self, board):
        if ((len(board.empty_spaces()) == len(board.spaces) - 1) 
            and board.space_is_empty(4)):
            return 4
        else:
            return 0

    def _make_best_choice(self, board):
        move = self._get_winning_move(board) 
        move = move or self._stop_immidate_loss(board) 
        move = move or self._make_good_choice(board) 
        return move

    def _deduce_opponent_marker(self, board):
        for space in range(0, len(board.spaces)):
            if (not board.space_is_empty(space) 
                and (board.spaces[space] != self.marker)):
                return board.spaces[space]

    def _get_move_weights(self, board):
        for space in board.empty_spaces():
            self.move_weights[space] = self._best_move(board, space)
        print(self.move_weights)


    # def _smart_move(self, board):
    #     if board.is_full(): 
    #         print("+0")
    #         return 0
    #     for space in board.empty_spaces():
    #         boardcopy = copy(board)
    #         weight = 0
    #         board.mark_space(space, self.marker)
    #         if winner(board) == self.marker: 
    #             print("+10")
    #             return 10
    #         for open_space in board.empty_spaces():
    #             secondcopy = copy(board)
    #             secondcopy.mark_space(open_space, self.opponent_marker)
    #             if winner(secondcopy) == self.opponent_marker: 
    #                 print("-10")
    #                 return -10
    #             weight += self._smart_move(secondcopy) 
    #         return weight

    def _best_move(self, board, set_move=None):
        if board.is_full():
            return 0
        weight = 0
        board2 = self._copy_the_board(board)
        if set_move:
            board2.mark_space(set_move, self.marker)
            if winner(board2): 
                return 10
        moves = board2.empty_spaces()
        for move in moves:
            boardcopy = self._copy_the_board(board2)
            if self._current_spaces(boardcopy, self.marker) <= self._current_spaces(boardcopy, self.opponent_marker):
                boardcopy.mark_space(move, self.marker)
                if winner(boardcopy):
                    return 10
                else:
                    weight += self._best_move(boardcopy)
            else:
                boardcopy.mark_space(move, self.opponent_marker)
                if winner(boardcopy):
                    return -10
                else:
                    weight += self._best_move(boardcopy)
        return weight

    def _copy_the_board(self, board):
        new_board = Board()
        for space in new_board.spaces:
            new_board.mark_space(space, board.spaces[space])
        return new_board

    def _current_spaces(self, board, marker):
        return len([space for space in range(0, len(board.spaces)) 
                if board.spaces[space] == marker])

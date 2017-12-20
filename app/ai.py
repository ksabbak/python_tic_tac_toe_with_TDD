from random import randint, choice
from copy import copy

from .player import Player
from .board import Board
from .end_conditions import winner, is_over

class AI(Player):
    
    def get_move(self, board):
        print(".... Hm. The computer is thinking")
        self.opponent_marker = self._deduce_opponent_marker(board) or chr(ord(self.marker) + 1)
        self.move_weights = {}
        self._get_move_weights(board)
        return self._pick_the_best_move()

    # PRIVATE METHODS

    # MINIMAX
    def _pick_the_best_move(self):
        best_spaces = []
        most_weight = list(self.move_weights.values())[0]
        print(self.move_weights)
        # self._handle_all_negative_move_weights()
        for space, weight in self.move_weights.items():
            if most_weight == weight:
                best_spaces.append(space)
            elif most_weight < weight:
                most_weight = weight 
                best_spaces = [space]
        if best_spaces:
            return choice(best_spaces)
    
    def _handle_all_negative_move_weights(self):
        for weight in self.move_weights.values():
            if weight > 0: return
        self.move_weights = {space: weight * -1 for space, weight in self.move_weights.items()}

    def _get_move_weights(self, board):
        for space in board.empty_spaces():
            self.move_weights[space] = self._weigh_move(board, space)

    def _weigh_move(self, board, set_move=None, turn="self"):
        if board.is_full(): return 0
        weight = 0
        board2 = self._copy_the_board(board)
        if set_move is not None:
            board2.mark_space(set_move, self.marker)
            turn = "other"
            if winner(board2): return 100000000000
        for move in board2.empty_spaces():
            boardcopy = self._copy_the_board(board2)
            if turn == "self":
                weight += self._calculate_move(boardcopy, move, self.marker, 10)
            else:
                weight += self._calculate_move(boardcopy, move, self.opponent_marker, -10)
        return weight

    def _calculate_move(self, board, move, marker, win_weight):
        # if self._make_immediate_vital_move(board, marker) is not None:
        #     weight = win_weight
        # else:
        board.mark_space(move, marker)
        if winner(board):
            weight = win_weight
        else:
            next_turn = "self" if win_weight < 0 else "other"
            weight = self._weigh_move(board, turn=next_turn)
        return weight

    def _make_immediate_vital_move(self, board, marker):
        for space in board.empty_spaces():
            copy_board = copy(board)
            copy_board.mark_space(space, marker)
            if winner(copy_board) == marker: return space

    # MECHANICS
    def _copy_the_board(self, board):
        new_board = Board()
        for space in new_board.spaces:
            new_board.mark_space(space, board.spaces[space])
        return new_board

    def _deduce_opponent_marker(self, board):
        for space in range(0, len(board.spaces)):
            if (not board.space_is_empty(space) 
                and (board.spaces[space] != self.marker)):
                return board.spaces[space]

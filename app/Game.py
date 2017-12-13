import sys
import math


from .board import Board
from .player import Player

class Game:
    def __init__(self, player1="x", player2="o"):
        self.board = Board()
        self.players = [Player(player1), Player(player2)]

    def is_over(self):
        winner = (self._horizontal_win_conditions() 
                  or self._vertical_win_conditions()
                  or self._diagonal_win_conditions())
        return self.board.is_full() or winner

    def _horizontal_win_conditions(self):
        return self._calculate_win_condition(1, self.board.side_length)
        # i = 0
        # while i < len(self.board.spaces):
        #     winner = (self.board.spaces[i] == self.board.spaces[i + 1] 
        #                and self.board.spaces[i] == self.board.spaces[i+2])
        #     if winner: return True
        #     i += 3
        # return False

    def _vertical_win_conditions(self):
        return self._calculate_win_condition(self.board.side_length, 1)
        # i = 0
        # while i < ( len(self.board.spaces) / 3):
        #     winner = (self.board.spaces[i] == self.board.spaces[i + 3] 
        #                and self.board.spaces[i] == self.board.spaces[i+6])
        #     if winner: return True
        #     i += 1
        # return False

    def _diagonal_win_conditions(self):
        return self._calculate_win_condition(self.board.side_length+1 , -2)
        # return ((self.board.spaces[0] == self.board.spaces[4] 
        #             and self.board.spaces[0] == self.board.spaces[8])
        #         or
        #         (self.board.spaces[2] == self.board.spaces[4] 
        #                and self.board.spaces[2] == self.board.spaces[6]))
        ####
        # i = 0
        # side_length = int((len(self.board.spaces)**(1/2)))
        # while i <= 2:
        #     winner = (self.board.spaces[i] == self.board.spaces[side_length + 1] 
        #                and self.board.spaces[i] == self.board.spaces[2 * (side_length + 1 - i)])
        #     if winner: return True
        #     i += 2
        # return False


    def _calculate_win_condition(self, addition, incrementor):
        i = 0
        while int(math.fabs(i)) < math.ceil(len(self.board.spaces) / addition):
            abs_i = int(math.fabs(i))
            winner = (self.board.spaces[abs_i] == self.board.spaces[i + addition] 
                       and self.board.spaces[abs_i] == self.board.spaces[i + 2*(addition)])
            if winner: return True
            i += incrementor
        return False



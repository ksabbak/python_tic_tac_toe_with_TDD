import sys
import math

from .board import Board
from .player import Player

class Game:
    def __init__(self, player1="x", player2="o"):
        self.board = Board()
        self.players = [Player(player1), Player(player2)]

    def play(self):
        print("Welcome!")
        print("this is tic-tac-toe!")
        i = 0
        while not self.is_over():
            current_player = self.players[i%2]
            move = current_player.get_move()
            self.board.mark_space(move, current_player.marker)
            print(self.board.to_str())
            i += 1
        print("Okay, the game is over")
        if self.winner(): print("%s wins!" % self.winner())

    def is_over(self):
        return not not (self.board.is_full() or self.winner())

    def winner(self):
        winner = (self._horizontal_win_conditions() 
          or self._vertical_win_conditions()
          or self._diagonal_win_conditions())
        return winner
        

    def _horizontal_win_conditions(self):
        return self._calculate_win_condition(1, self.board.side_length)

    def _vertical_win_conditions(self):
        return self._calculate_win_condition(self.board.side_length, 1)


    def _diagonal_win_conditions(self):
        return self._calculate_win_condition(self.board.side_length+1 , -2)

    def _calculate_win_condition(self, addition, incrementor):
        i = 0
        while int(math.fabs(i)) < math.ceil(len(self.board.spaces) / addition):
            abs_i = int(math.fabs(i))
            winner = (self.board.spaces[abs_i] == self.board.spaces[i + addition] 
                       and self.board.spaces[abs_i] == self.board.spaces[i + 2*(addition)])
            if winner: return self.board.spaces[abs_i]
            i += incrementor



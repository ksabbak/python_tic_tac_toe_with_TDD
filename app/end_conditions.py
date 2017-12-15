import math

def winner(board):
    winner = (_horizontal_win_conditions(board) 
      or _vertical_win_conditions(board)
      or _diagonal_win_conditions(board))
    return winner
    

def _horizontal_win_conditions(board):
    return _calculate_win_conditions(board, 1, board.side_length)

def _vertical_win_conditions(board):
    return _calculate_win_conditions(board, board.side_length, 1)


def _diagonal_win_conditions(board):
    return _calculate_win_conditions(board, board.side_length+1 , -2)

def _calculate_win_conditions(board, addition, incrementor):
    i = 0
    while int(math.fabs(i)) < math.ceil(len(board.spaces) / addition):
        abs_i = int(math.fabs(i))
        winner = (board.spaces[abs_i] == board.spaces[i + addition] 
                   and board.spaces[abs_i] == board.spaces[i + 2*(addition)])
        if winner: return board.spaces[abs_i]
        i += incrementor

def is_over(board):
    return not not (board.is_full() or winner(board))

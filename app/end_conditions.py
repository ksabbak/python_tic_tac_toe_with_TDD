import math

def winning_marker(board):
    winner = (_horizontal_win_conditions(board) 
      or _vertical_win_conditions(board)
      or _diagonal_win_conditions(board))
    return winner
    

def _horizontal_win_conditions(board):
    return _calculate_win_conditions(board, 1, board.side_length)

def _vertical_win_conditions(board):
    return _calculate_win_conditions(board, board.side_length, 1)


def _diagonal_win_conditions(board):
    win =  (board.spaces[0] == board.spaces[4] 
            and board.spaces[0] == board.spaces[8])
    win = (win or (board.spaces[2] == board.spaces[4] 
                    and board.spaces[2] == board.spaces[6]))
    if win and not board.space_is_empty(4): return board.spaces[4]

def _calculate_win_conditions(board, addition, incrementor):
    i = 0
    while i < (len(board.spaces) / addition):
        winner = (board.spaces[i] == board.spaces[i + addition] 
                   and board.spaces[i] == board.spaces[i + 2*(addition)])
        if winner and not board.space_is_empty(i): return board.spaces[i]
        i += incrementor

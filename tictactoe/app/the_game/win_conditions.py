
def all_win_conditions(board):
    all_win_conditions = _horizontal_win_conditions(board) + _vertical_win_conditions(board) + _diagonal_win_conditions(board)
    return all_win_conditions

def _horizontal_win_conditions(board):
    wins = []
    for i in range(0, board.side_length()):
        wins.append(_calculate_win_conditions(board, 1, board.side_length() * i))
    return wins

def _vertical_win_conditions(board):
    wins = []
    for i in range(0, board.side_length()):
        wins.append(_calculate_win_conditions(board, board.side_length(), i))
    return wins

def _diagonal_win_conditions(board):
    wins = []
    wins.append(_calculate_win_conditions(board, board.side_length() + 1, 0))
    wins.append(_calculate_win_conditions(board, board.side_length() - 1, board.side_length() - 1))
    return wins

def _calculate_win_conditions(board, incrementor, addition):
    lst = []
    for space in range(0, board.side_length()):
        lst.append(space * incrementor + addition)
    return lst

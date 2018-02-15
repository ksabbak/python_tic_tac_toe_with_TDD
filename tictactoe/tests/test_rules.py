import pytest

from tictactoe.app.__init__ import Board, Rules


@pytest.fixture()
def board():
    board = Board.create_fresh_board()
    return board

@pytest.fixture()
def big_board():
    board = Board.create_fresh_board(16)
    return board

@pytest.fixture()
def rules_for_3x3(board):
    return Rules(board)

@pytest.fixture()
def rules_for_4x4(big_board):
    return Rules(big_board)

def test_game_knows_winner_9_space_board(board, rules_for_3x3):
    board.mark_space(0, 0)
    board.mark_space(1, 2)
    board.mark_space(2, 4)
    assert rules_for_3x3.winning_marker() == 0

def test_game_knows_winner_mixed_board_9_space_board(board, rules_for_3x3):
    board.mark_space(0, 0)
    board.mark_space(1, 2)
    board.mark_space(2, 1)
    assert rules_for_3x3.winning_marker() is None

def test_game_knows_winner_mixed_board_9_space_board(board, rules_for_3x3):
    board.mark_space(2, 0)
    board.mark_space(6, 2)
    board.mark_space(4, 1)
    board.mark_space(5, 3)
    assert rules_for_3x3.winning_marker() is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_9_space_board(board, rules_for_3x3):
    board.mark_space(0, 2)
    board.mark_space(1, 2)
    board.mark_space(2, 2)
    assert rules_for_3x3.winning_marker() == 0

def test_game_over_for_horizontal_win_2nd_row_9_space_board(board, rules_for_3x3):
    board.mark_space(3, 0)
    board.mark_space(4, 0)
    board.mark_space(5, 0)
    assert rules_for_3x3.winning_marker() == 0

def test_game_over_for_horizontal_win_3nd_row_9_space_board(board, rules_for_3x3):
    board.mark_space(6, 0)
    board.mark_space(7, 0)
    board.mark_space(8, 0)
    assert rules_for_3x3.winning_marker() == 0

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_9_space_board(board, rules_for_3x3):
    board.mark_space(0, 0)
    board.mark_space(3, 0)
    board.mark_space(6, 0)
    assert rules_for_3x3.winning_marker() == 0

def test_game_over_for_vertical_win_2nd_col_9_space_board(board, rules_for_3x3):
    board.mark_space(1, 0)
    board.mark_space(4, 0)
    board.mark_space(7, 0)
    assert rules_for_3x3.winning_marker() == 0

def test_game_over_for_vertical_win_3nd_col_9_space_board(board, rules_for_3x3):
    board.mark_space(2, 0)
    board.mark_space(5, 0)
    board.mark_space(8, 0)
    assert rules_for_3x3.winning_marker() == 0

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_9_space_board(board, rules_for_3x3):
    board.mark_space(0, 0)
    board.mark_space(4, 0)
    board.mark_space(8, 0)
    assert rules_for_3x3.winning_marker() == 0

def test_game_over_for_diagonal_win_right_to_left_9_space_board(board, rules_for_3x3):
    board.mark_space(2, 0)
    board.mark_space(4, 0)
    board.mark_space(6, 0)
    assert rules_for_3x3.winning_marker() == 0

# Big Board:

def test_game_knows_winner_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, 0)
    big_board.mark_space(1, 2)
    big_board.mark_space(2, 4)
    big_board.mark_space(3, 6)
    assert rules_for_4x4.winning_marker() == 0

def test_game_knows_winner_mixed_board_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, 0)
    big_board.mark_space(1, 2)
    big_board.mark_space(2, 1)
    big_board.mark_space(3, 4)
    assert rules_for_4x4.winning_marker() is None

def test_game_knows_winner_mixed_board_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(2, 0)
    big_board.mark_space(6, 2)
    big_board.mark_space(4, 1)
    big_board.mark_space(5, 3)
    assert rules_for_4x4.winning_marker() is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, 0)
    big_board.mark_space(1, 0)
    big_board.mark_space(2, 0)
    big_board.mark_space(3, 0)
    assert rules_for_4x4.winning_marker() == 0

def test_game_over_for_horizontal_win_last_row_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(12, 0)
    big_board.mark_space(13, 0)
    big_board.mark_space(14, 0)
    big_board.mark_space(15, 0)
    assert rules_for_4x4.winning_marker() == 0

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, 0)
    big_board.mark_space(4, 0)
    big_board.mark_space(8, 0)
    big_board.mark_space(12, 0)
    assert rules_for_4x4.winning_marker() == 0

def test_game_over_for_vertical_win_last_col_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(3, 4)
    big_board.mark_space(7, 4)
    big_board.mark_space(11, 4)
    big_board.mark_space(15, 4)
    assert rules_for_4x4.winning_marker() == 0

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(3, 4)
    big_board.mark_space(6, 4)
    big_board.mark_space(9, 4)
    big_board.mark_space(12, 4)
    assert rules_for_4x4.winning_marker() == 0

def test_game_over_for_diagonal_win_right_to_left_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, 4)
    big_board.mark_space(5, 4)
    big_board.mark_space(10, 4)
    big_board.mark_space(15, 4)
    assert rules_for_4x4.winning_marker() == 0

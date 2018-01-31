import pytest

from tictactoe.app.__init__ import Board
from tictactoe.app.rules import Rules


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
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    board.mark_space(2, "x")
    assert rules_for_3x3.winning_marker() == "x"

def test_game_knows_winner_mixed_board_9_space_board(board, rules_for_3x3):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    board.mark_space(2, "o")
    assert rules_for_3x3.winning_marker() is None

def test_game_knows_winner_mixed_board_9_space_board(board, rules_for_3x3):
    board.mark_space(2, "x")
    board.mark_space(6, "x")
    board.mark_space(4, "o")
    board.mark_space(5, "o")
    assert rules_for_3x3.winning_marker() is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_9_space_board(board, rules_for_3x3):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    board.mark_space(2, "x")
    assert rules_for_3x3.winning_marker() == "x"

def test_game_over_for_horizontal_win_2nd_row_9_space_board(board, rules_for_3x3):
    board.mark_space(3, "x")
    board.mark_space(4, "x")
    board.mark_space(5, "x")
    assert rules_for_3x3.winning_marker() == "x"

def test_game_over_for_horizontal_win_3nd_row_9_space_board(board, rules_for_3x3):
    board.mark_space(6, "x")
    board.mark_space(7, "x")
    board.mark_space(8, "x")
    assert rules_for_3x3.winning_marker() == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_9_space_board(board, rules_for_3x3):
    board.mark_space(0, "x")
    board.mark_space(3, "x")
    board.mark_space(6, "x")
    assert rules_for_3x3.winning_marker() == "x"

def test_game_over_for_vertical_win_2nd_col_9_space_board(board, rules_for_3x3):
    board.mark_space(1, "x")
    board.mark_space(4, "x")
    board.mark_space(7, "x")
    assert rules_for_3x3.winning_marker() == "x"

def test_game_over_for_vertical_win_3nd_col_9_space_board(board, rules_for_3x3):
    board.mark_space(2, "x")
    board.mark_space(5, "x")
    board.mark_space(8, "x")
    assert rules_for_3x3.winning_marker() == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_9_space_board(board, rules_for_3x3):
    board.mark_space(0, "x")
    board.mark_space(4, "x")
    board.mark_space(8, "x")
    assert rules_for_3x3.winning_marker() == "x"

def test_game_over_for_diagonal_win_right_to_left_9_space_board(board, rules_for_3x3):
    board.mark_space(2, "x")
    board.mark_space(4, "x")
    board.mark_space(6, "x")
    assert rules_for_3x3.winning_marker() == "x"

# Big Board:

def test_game_knows_winner_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "x")
    big_board.mark_space(3, "x")
    assert rules_for_4x4.winning_marker() == "x"

def test_game_knows_winner_mixed_board_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "o")
    big_board.mark_space(3, "x")
    assert rules_for_4x4.winning_marker() is None

def test_game_knows_winner_mixed_board_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(2, "x")
    big_board.mark_space(6, "x")
    big_board.mark_space(4, "o")
    big_board.mark_space(5, "o")
    assert rules_for_4x4.winning_marker() is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "x")
    big_board.mark_space(3, "x")
    assert rules_for_4x4.winning_marker() == "x"

def test_game_over_for_horizontal_win_last_row_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(12, "x")
    big_board.mark_space(13, "x")
    big_board.mark_space(14, "x")
    big_board.mark_space(15, "x")
    assert rules_for_4x4.winning_marker() == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, "x")
    big_board.mark_space(4, "x")
    big_board.mark_space(8, "x")
    big_board.mark_space(12, "x")
    assert rules_for_4x4.winning_marker() == "x"

def test_game_over_for_vertical_win_last_col_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(3, "x")
    big_board.mark_space(7, "x")
    big_board.mark_space(11, "x")
    big_board.mark_space(15, "x")
    assert rules_for_4x4.winning_marker() == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(3, "x")
    big_board.mark_space(6, "x")
    big_board.mark_space(9, "x")
    big_board.mark_space(12, "x")
    assert rules_for_4x4.winning_marker() == "x"

def test_game_over_for_diagonal_win_right_to_left_16_space_board(big_board, rules_for_4x4):
    big_board.mark_space(0, "x")
    big_board.mark_space(5, "x")
    big_board.mark_space(10, "x")
    big_board.mark_space(15, "x")
    assert rules_for_4x4.winning_marker() == "x"

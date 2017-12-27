import sys
import pytest
import io

from ..app.__init__ import Game, Board
from ..app.end_conditions import winning_marker

@pytest.fixture()
def game():
    return Game()

def test_game_knows_winner_9_space_board(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(1, "x")
    game.board.mark_space(2, "x")
    assert winning_marker(game.board) == "x"

def test_game_knows_winner_mixed_board_9_space_board(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(1, "x")
    game.board.mark_space(2, "o")
    assert winning_marker(game.board) is None

def test_game_knows_winner_mixed_board_9_space_board(game):
    game.board.mark_space(2, "x")
    game.board.mark_space(6, "x")
    game.board.mark_space(4, "o")
    game.board.mark_space(5, "o")
    assert winning_marker(game.board) is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_9_space_board(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(1, "x")
    game.board.mark_space(2, "x")
    assert winning_marker(game.board) == "x"

def test_game_over_for_horizontal_win_2nd_row_9_space_board(game):
    game.board.mark_space(3, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(5, "x")
    assert winning_marker(game.board) == "x"

def test_game_over_for_horizontal_win_3nd_row_9_space_board(game):
    game.board.mark_space(6, "x")
    game.board.mark_space(7, "x")
    game.board.mark_space(8, "x")
    assert winning_marker(game.board) == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_9_space_board(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(3, "x")
    game.board.mark_space(6, "x")
    assert winning_marker(game.board) == "x"

def test_game_over_for_vertical_win_2nd_col_9_space_board(game):
    game.board.mark_space(1, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(7, "x")
    assert winning_marker(game.board) == "x"

def test_game_over_for_vertical_win_3nd_col_9_space_board(game):
    game.board.mark_space(2, "x")
    game.board.mark_space(5, "x")
    game.board.mark_space(8, "x")
    assert winning_marker(game.board) == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_9_space_board(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(8, "x")
    assert winning_marker(game.board) == "x"

def test_game_over_for_diagonal_win_right_to_left_9_space_board(game):
    game.board.mark_space(2, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(6, "x")
    assert winning_marker(game.board) == "x"


@pytest.fixture()
def big_board():
    board = Board(16)
    return board

def test_game_knows_winner_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "x")
    big_board.mark_space(3, "x")
    assert winning_marker(big_board) == "x"

def test_game_knows_winner_mixed_board_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "o")
    big_board.mark_space(3, "x")
    assert winning_marker(big_board) is None

def test_game_knows_winner_mixed_board_16_space_board(big_board):
    big_board.mark_space(2, "x")
    big_board.mark_space(6, "x")
    big_board.mark_space(4, "o")
    big_board.mark_space(5, "o")
    assert winning_marker(big_board) is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "x")
    big_board.mark_space(3, "x")
    assert winning_marker(big_board) == "x"

def test_game_over_for_horizontal_win_last_row_16_space_board(big_board):
    big_board.mark_space(12, "x")
    big_board.mark_space(13, "x")
    big_board.mark_space(14, "x")
    big_board.mark_space(15, "x")
    assert winning_marker(big_board) == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(4, "x")
    big_board.mark_space(8, "x")
    big_board.mark_space(12, "x")
    assert winning_marker(big_board) == "x"

def test_game_over_for_vertical_win_last_col_16_space_board(big_board):
    big_board.mark_space(3, "x")
    big_board.mark_space(7, "x")
    big_board.mark_space(11, "x")
    big_board.mark_space(15, "x")
    assert winning_marker(big_board) == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_16_space_board(big_board):
    big_board.mark_space(3, "x")
    big_board.mark_space(6, "x")
    big_board.mark_space(9, "x")
    big_board.mark_space(12, "x")
    assert winning_marker(big_board) == "x"

def test_game_over_for_diagonal_win_right_to_left_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(5, "x")
    big_board.mark_space(10, "x")
    big_board.mark_space(15, "x")
    assert winning_marker(big_board) == "x"

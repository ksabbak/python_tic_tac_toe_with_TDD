import sys
import pytest
import io

from ..app.__init__ import Game
from ..app.win_conditions import winner

@pytest.fixture()
def game():
    return Game()

def test_game_knows_winner(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(1, "x")
    game.board.mark_space(2, "x")
    assert winner(game.board) == "x"

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(1, "x")
    game.board.mark_space(2, "x")
    assert winner(game.board) == "x"

def test_game_over_for_horizontal_win_2nd_row(game):
    game.board.mark_space(3, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(5, "x")
    assert winner(game.board) == "x"

def test_game_over_for_horizontal_win_3nd_row(game):
    game.board.mark_space(6, "x")
    game.board.mark_space(7, "x")
    game.board.mark_space(8, "x")
    assert winner(game.board) == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(3, "x")
    game.board.mark_space(6, "x")
    assert winner(game.board) == "x"

def test_game_over_for_vertical_win_2nd_col(game):
    game.board.mark_space(1, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(7, "x")
    assert winner(game.board) == "x"

def test_game_over_for_vertical_win_3nd_col(game):
    game.board.mark_space(2, "x")
    game.board.mark_space(5, "x")
    game.board.mark_space(8, "x")
    assert winner(game.board) == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(8, "x")
    assert winner(game.board) == "x"

def test_game_over_for_diagonal_win_right_to_left(game):
    game.board.mark_space(2, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(6, "x")
    assert winner(game.board) == "x"

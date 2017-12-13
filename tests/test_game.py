import pytest

from ..app.__init__ import Game

@pytest.fixture()
def game():
    return Game()

# GENERAL
def test_there_is_a_game(game):
    assert game is not None

def test_game_over_for_horizontal_win_first_row(game):
    game.board.mark_space(0, "x")
    game.board.mark_space(1, "x")
    game.board.mark_space(2, "x")
    print(game.is_over())
    assert game.is_over()

def test_game_over_for_horizontal_win_2nd_row(game):
    game.board.mark_space(3, "x")
    game.board.mark_space(4, "x")
    game.board.mark_space(5, "x")
    print(game.is_over())
    assert game.is_over()


# BOARD
def test_game_has_board(game):
    assert game.board is not None

def test_game_is_marked_over_when_board_is_filled(game):
    i = 0
    while i < len(game.board.spaces):
        game.board.mark_space(i, "X")
        i += 1
    assert game.is_over()

#PLAYERS
def test_game_has_two_players(game):
    assert len(game.players) == 2

def test_player_one_has_marker_x(game):
    assert game.players[0].marker == "x"

def test_player_two_has_marker_o(game):
    assert game.players[1].marker == "o"

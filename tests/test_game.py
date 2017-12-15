import sys
import pytest
import io

from ..app.__init__ import Game

@pytest.fixture()
def game():
    return Game()

# GENERAL
def test_there_is_a_game(game):
    assert game is not None

# BOARD
def test_game_has_board(game):
    assert game.board is not None

#PLAYERS
def test_game_has_two_players(game):
    assert len(game.players) == 2

def test_player_one_has_marker_x(game):
    assert game.players[0].marker == "x"

def test_player_two_has_marker_o(game):
    assert game.players[1].marker == "o"

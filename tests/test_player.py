import pytest
import unittest
from unittest.mock import patch
# from unittest import TestCase

from ..app.__init__ import Player, HumanPlayer, Board

# class TestPlayer(TestCase):

@pytest.fixture()
def human_playerx():
    return HumanPlayer("x")

def test_players_have_markers():
    assert Player("?").marker is not None
    assert Player("!").marker == "!"

def test_human_player_is_not_ai(human_playerx):
    assert human_playerx.is_ai() is False

def test_human_player_has_move_log(human_playerx):
    assert human_playerx.moves == []

def test_human_player_logs_moves(human_playerx):
    board = Board()
    human_playerx.make_move(board, 8)
    human_playerx.make_move(board, 0)
    human_playerx.make_move(board, 4)
    assert human_playerx.moves == [8, 0, 4]

# @patch('builtins.print', return_value="")
def xtest_get_move(human_playerx):
    with unittest.mock.patch('builtins.input', return_value='7'):
        assert human_playerx.get_move() == 7

import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.__init__ import Player, HumanPlayer, Board

@pytest.fixture()
def human_player():
    return HumanPlayer(0)

def test_human_player_is_not_ai(human_player):
    assert human_player.is_ai() is False

def xtest_get_move(human_player):
    with unittest.mock.patch('builtins.input', return_value='7'):
        assert human_player.get_move() == 7

def test_human_player_knows_turn_order(human_player):
    assert human_player.turn_order == 0

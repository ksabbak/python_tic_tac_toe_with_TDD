import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.__init__ import Player, HumanPlayer, Board

@pytest.fixture()
def human_playerx():
    return HumanPlayer()

def test_human_player_is_not_ai(human_playerx):
    assert human_playerx.is_ai() is False

def xtest_get_move(human_playerx):
    with unittest.mock.patch('builtins.input', return_value='7'):
        assert human_playerx.get_move() == 7

import pytest
import unittest
from unittest.mock import patch
# from unittest import TestCase

from ..app.__init__ import Player

# class TestPlayer(TestCase):

@pytest.fixture()
def playerx():
    return Player("x")

def test_players_have_markers():
    assert Player("?").marker is not None

# @patch('builtins.print', return_value="")
def test_get_move(playerx):
    with unittest.mock.patch('builtins.input', return_value='7'):
        assert playerx.get_move() == 7

from unittest.mock import patch

from ..app.__init__ import Player

@pytest.fixture()
def playerx():
    return Player("x")

def test_players_have_markers():
    assert Player("?").marker is not None

@patch('player.get_input', return_value=7)
def test_get_move(playerx):
    assert playerx.get_move() == 7

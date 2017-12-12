from ..app.__init__ import Player

def test_players_have_markers():
    assert Player().marker is not None

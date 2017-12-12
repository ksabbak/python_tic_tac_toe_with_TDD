from ..app.Game import Game

def test_there_is_a_game():
    assert Game() is not None

def test_game_has_board():
    assert Game().board is not None

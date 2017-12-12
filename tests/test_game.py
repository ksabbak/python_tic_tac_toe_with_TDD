from ..app.game import Game

def test_there_is_a_game():
    assert Game() is not None

def test_game_has_board():
    assert Game().board is not None

def test_game_has_players():
    assert len(Game().players) == 2

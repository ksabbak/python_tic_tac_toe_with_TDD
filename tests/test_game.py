from ..app.game import Game


# GENERAL
def test_there_is_a_game():
    assert Game() is not None

# BOARD
def test_game_has_board():
    assert Game().board is not None

#PLAYERS
def test_game_has_two_players():
    assert len(Game().players) == 2

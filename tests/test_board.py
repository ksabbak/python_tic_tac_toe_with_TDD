from ..app.game import Game

    
def test_board_has_9_spaces():
    assert len(Board().spaces) == 9

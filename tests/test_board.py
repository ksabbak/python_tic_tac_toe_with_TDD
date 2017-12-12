from ..app.__init__ import Board

    
def test_board_has_9_spaces():
    assert len(Board().spaces) == 9

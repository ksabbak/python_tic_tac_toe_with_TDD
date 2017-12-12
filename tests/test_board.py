from ..app.__init__ import Board

    
def test_board_has_9_spaces():
    assert len(Board().spaces) == 9

def test_board_can_mark_space():
    board = Board()
    board.mark_space(1, "x")
    assert board.spaces[1] == "x"

def test_board_does_not_remark_space():
    board = Board()
    board.mark_space(1, "x")
    board.mark_space(1, "o")
    assert board.spaces[1] == "x"

def test_board_knows_when_full():
    board = Board()
    assert not board.is_full()
    i = 0
    while i < len(board.spaces):
        board.mark_space(i, "X")
        i += 1
    assert board.is_full()


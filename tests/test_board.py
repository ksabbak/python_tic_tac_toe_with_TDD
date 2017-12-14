import pytest

from ..app.__init__ import Board

@pytest.fixture()
def board():
    board = Board()
    return board

    
def test_board_has_9_spaces(board):
    assert len(board.spaces) == 9

def test_board_can_mark_space(board):
    board.mark_space(1, "x")
    assert board.spaces[1] == "x"

def test_board_does_not_remark_space(board):
    board.mark_space(1, "x")
    board.mark_space(1, "o")
    assert board.spaces[1] == "x"

def test_board_knows_when_full(board):
    assert not board.is_full()
    i = 0
    while i < len(board.spaces):
        board.mark_space(i, "X")
        i += 1
    assert board.is_full()

def test_board_pretty_print(board):
     assert board.pretty_print() == " 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n" 

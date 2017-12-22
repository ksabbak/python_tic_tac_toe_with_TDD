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
    assert board.is_full() is True

def test_board_knows_when_space_is_empty(board):
    assert board.space_is_empty(0)
    board.mark_space(0, "x")
    assert board.space_is_empty(0) is False

def test_board_to_str(board):
     assert board.to_str() == " 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n" 

def test_board_knows_all_empty_spaces(board):
    assert board.empty_spaces() == list(board.spaces)
    assert len(board.empty_spaces()) == 9
    board.mark_space(1, "!")
    expected_spaces = list(board.spaces)
    expected_spaces.remove("!")
    assert board.empty_spaces() == expected_spaces
    assert len(board.empty_spaces()) == 8

def test_build_board_length(board):
    board._build_board(5)
    assert len(board.spaces) == 5

import io
import pytest
from textwrap import dedent

from tictactoe.app.__init__ import Board


@pytest.fixture()
def board():
    board = Board.create_fresh_board()
    return board

@pytest.fixture()
def big_board():
    board = Board.create_fresh_board(16)
    return board

def test_create_from_existing_is_new_board(board):
    new_board = Board.create_from_existing_spaces(board.spaces)
    assert new_board.__class__.__name__ == "Board"
    assert new_board != board

def test_board_has_9_spaces(board):
    assert len(board.spaces) == 9

def test_board_can_mark_space(board):
    board.mark_space(1, 0)
    assert board.spaces[1] == 0

def test_board_can_clear_space(board):
    board.mark_space(1, 0)
    board.clear_space(1)
    assert board.spaces[1] == " "

def test_board_does_not_remark_space(board):
    board.mark_space(1, 0)
    board.mark_space(1, 1)
    assert board.spaces[1] == 0

def test_board_knows_when_full(board):
    assert not board.is_full()
    i = 0
    while i < len(board.spaces):
        board.mark_space(i, 0)
        i += 1
    assert board.is_full() is True

def test_board_knows_when_space_is_empty(board, big_board):
    assert board.space_is_empty(0)
    board.mark_space(0, 0)
    assert board.space_is_empty(0) is False
    assert big_board.space_is_empty(13)
    big_board.mark_space(13, 2)
    assert big_board.space_is_empty(13) is False

def test_space_string(board):
    assert board.space_string() == "         "
    board.mark_space(0, 0)
    assert board.space_string() == "0        "

def test_board_knows_all_empty_spaces(board):
    assert board.empty_spaces() == list(range(0, 9))
    assert len(board.empty_spaces()) == 9
    board.mark_space(1, 0)
    expected_spaces = [0, 2, 3, 4, 5, 6, 7, 8]
    assert board.empty_spaces() == expected_spaces
    assert len(board.empty_spaces()) == 8

def test_board_knows_all_empty_spaces_4x4(big_board):
    board = big_board
    assert board.empty_spaces() == list(range(0, 16))
    assert len(board.empty_spaces()) == 16
    board.mark_space(1, 0)
    board.mark_space(15, 2)
    expected_spaces = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert board.empty_spaces() == expected_spaces
    assert len(board.empty_spaces()) == 14

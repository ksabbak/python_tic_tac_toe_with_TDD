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
    board.mark_space(1, "x")
    assert board.spaces[1] == "x"

def test_board_can_clear_space(board):
    board.mark_space(1, "x")
    board.clear_space(1)
    assert board.spaces[1] == " "

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

def test_board_knows_when_space_is_empty(board, big_board):
    assert board.space_is_empty(0)
    board.mark_space(0, "x")
    assert board.space_is_empty(0) is False
    assert big_board.space_is_empty(13)
    big_board.mark_space(13, "x")
    assert big_board.space_is_empty(13) is False

def test_space_string(board):
    assert board.space_string() == "         "

def test_board_knows_all_empty_spaces(board):
    assert board.empty_spaces() == list(range(0, 9))
    assert len(board.empty_spaces()) == 9
    board.mark_space(1, "!")
    expected_spaces = [0, 2, 3, 4, 5, 6, 7, 8]
    assert board.empty_spaces() == expected_spaces
    assert len(board.empty_spaces()) == 8

def test_board_knows_all_empty_spaces_4x4(big_board):
    board = big_board
    assert board.empty_spaces() == list(range(0, 16))
    assert len(board.empty_spaces()) == 16
    board.mark_space(1, "!")
    board.mark_space(15, "!")
    expected_spaces = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert board.empty_spaces() == expected_spaces
    assert len(board.empty_spaces()) == 14

def test_build_coordinates(board, big_board):
    assert board.coordinates == ['A1', 'A2', 'A3',
                                 'B1', 'B2', 'B3',
                                 'C1', 'C2', 'C3'
                                 ]
    assert big_board.coordinates == ['A1', 'A2', 'A3', 'A4',
                                     'B1', 'B2', 'B3', 'B4',
                                     'C1', 'C2', 'C3', 'C4',
                                     'D1', 'D2', 'D3', 'D4'
                                     ]

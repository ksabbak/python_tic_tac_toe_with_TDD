import io
import pytest
from textwrap import dedent

from ..app.__init__ import Board


@pytest.fixture()
def board():
    board = Board.create_from_scratch()
    return board

@pytest.fixture()
def big_board():
    board = Board.create_from_scratch(16)
    return board

def test_create_from_existing_is_new_board(board):
    new_board = Board.create_from_existing(board.spaces)
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

def test_board_to_str_empty(board, big_board):
    pretty_board = """\
           1   2   3
        A    |   |   
          ===+===+===
        B    |   |   
          ===+===+===
        C    |   |   
        """
    assert str(board) == dedent(pretty_board)
    pretty_big_board = """\
           1   2   3   4
        A    |   |   |   
          ===+===+===+===
        B    |   |   |   
          ===+===+===+===
        C    |   |   |   
          ===+===+===+===
        D    |   |   |   
        """
    assert str(big_board) == dedent(pretty_big_board)

def test_board_to_str_marked(board, big_board):
    board.mark_space(4, "x")
    pretty_board = """\
           1   2   3
        A    |   |   
          ===+===+===
        B    | x |   
          ===+===+===
        C    |   |   
        """
    assert str(board) == dedent(pretty_board)
    big_board.mark_space(4, "x")
    pretty_big_board = """\
           1   2   3   4
        A    |   |   |   
          ===+===+===+===
        B  x |   |   |   
          ===+===+===+===
        C    |   |   |   
          ===+===+===+===
        D    |   |   |   
        """
    assert str(big_board) == dedent(pretty_big_board)

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


#END CONDITIONS:


def test_game_knows_winner_9_space_board(board):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    board.mark_space(2, "x")
    assert board.winning_marker() == "x"

def test_game_knows_winner_mixed_board_9_space_board(board):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    board.mark_space(2, "o")
    assert board.winning_marker() is None

def test_game_knows_winner_mixed_board_9_space_board(board):
    board.mark_space(2, "x")
    board.mark_space(6, "x")
    board.mark_space(4, "o")
    board.mark_space(5, "o")
    assert board.winning_marker() is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_9_space_board(board):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    board.mark_space(2, "x")
    assert board.winning_marker() == "x"

def test_game_over_for_horizontal_win_2nd_row_9_space_board(board):
    board.mark_space(3, "x")
    board.mark_space(4, "x")
    board.mark_space(5, "x")
    assert board.winning_marker() == "x"

def test_game_over_for_horizontal_win_3nd_row_9_space_board(board):
    board.mark_space(6, "x")
    board.mark_space(7, "x")
    board.mark_space(8, "x")
    assert board.winning_marker() == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_9_space_board(board):
    board.mark_space(0, "x")
    board.mark_space(3, "x")
    board.mark_space(6, "x")
    assert board.winning_marker() == "x"

def test_game_over_for_vertical_win_2nd_col_9_space_board(board):
    board.mark_space(1, "x")
    board.mark_space(4, "x")
    board.mark_space(7, "x")
    assert board.winning_marker() == "x"

def test_game_over_for_vertical_win_3nd_col_9_space_board(board):
    board.mark_space(2, "x")
    board.mark_space(5, "x")
    board.mark_space(8, "x")
    assert board.winning_marker() == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_9_space_board(board):
    board.mark_space(0, "x")
    board.mark_space(4, "x")
    board.mark_space(8, "x")
    assert board.winning_marker() == "x"

def test_game_over_for_diagonal_win_right_to_left_9_space_board(board):
    board.mark_space(2, "x")
    board.mark_space(4, "x")
    board.mark_space(6, "x")
    assert board.winning_marker() == "x"

# Big Board: 

def test_game_knows_winner_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "x")
    big_board.mark_space(3, "x")
    assert big_board.winning_marker() == "x"

def test_game_knows_winner_mixed_board_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "o")
    big_board.mark_space(3, "x")
    assert big_board.winning_marker() is None

def test_game_knows_winner_mixed_board_16_space_board(big_board):
    big_board.mark_space(2, "x")
    big_board.mark_space(6, "x")
    big_board.mark_space(4, "o")
    big_board.mark_space(5, "o")
    assert big_board.winning_marker() is None

# Horizontal win ends game
def test_game_over_for_horizontal_win_first_row_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(2, "x")
    big_board.mark_space(3, "x")
    assert big_board.winning_marker() == "x"

def test_game_over_for_horizontal_win_last_row_16_space_board(big_board):
    big_board.mark_space(12, "x")
    big_board.mark_space(13, "x")
    big_board.mark_space(14, "x")
    big_board.mark_space(15, "x")
    assert big_board.winning_marker() == "x"

# Vertical win ends game
def test_game_over_for_vertical_win_first_col_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(4, "x")
    big_board.mark_space(8, "x")
    big_board.mark_space(12, "x")
    assert big_board.winning_marker() == "x"

def test_game_over_for_vertical_win_last_col_16_space_board(big_board):
    big_board.mark_space(3, "x")
    big_board.mark_space(7, "x")
    big_board.mark_space(11, "x")
    big_board.mark_space(15, "x")
    assert big_board.winning_marker() == "x"

# Diagonal win ends game
def test_game_over_for_diagonal_win_left_to_right_16_space_board(big_board):
    big_board.mark_space(3, "x")
    big_board.mark_space(6, "x")
    big_board.mark_space(9, "x")
    big_board.mark_space(12, "x")
    assert big_board.winning_marker() == "x"

def test_game_over_for_diagonal_win_right_to_left_16_space_board(big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(5, "x")
    big_board.mark_space(10, "x")
    big_board.mark_space(15, "x")
    assert big_board.winning_marker() == "x"


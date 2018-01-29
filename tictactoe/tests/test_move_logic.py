import pytest

from tictactoe.app.__init__ import Board
from tictactoe.app.move_logic import MoveLogic

@pytest.fixture()
def board():
    return Board.create_fresh_board()
@pytest.fixture()
def move_logic(board):
    return MoveLogic("x", board)

def tests_move_logic_can_move_without_input(move_logic, board):
    assert move_logic.get_move() in range(0, 9)

def tests_move_logic_moves_to_empty_spot(move_logic, board):
    for i in range(1, 9):
        board.mark_space(i, "x")
    assert move_logic.get_move() == 0

def test_move_logic_can_make_winning_move(move_logic, board):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    assert move_logic.get_move() == 2

def test_move_logic_can_stop_immediate_horizontal_loss0(move_logic, board):
    board.mark_space(3, "o")
    board.mark_space(0, "x")
    board.mark_space(4, "o")
    assert move_logic.get_move() == 5

def test_move_logic_can_stop_immediate_horizontal_loss2(move_logic, board):
    board.mark_space(3, "o")
    board.mark_space(2, "x")
    board.mark_space(4, "o")
    assert move_logic.get_move() == 5

def test_move_logic_can_stop_immediate_horizontal_loss6(move_logic, board):
    board.mark_space(3, "o")
    board.mark_space(6, "x")
    board.mark_space(4, "o")
    assert move_logic.get_move() == 5

def test_move_logic_can_stop_immediate_horizontal_loss8(move_logic, board):
    board.mark_space(3, "o")
    board.mark_space(8, "x")
    board.mark_space(4, "o")
    assert move_logic.get_move() == 5

def test_move_logic_1st_move_when_1st_is_center(move_logic, board):
    assert move_logic.get_move() == 4

def test_move_logic_1st_move_when_2nd_is_middle_space_if_open(move_logic, board):
    board.mark_space(3, "o")
    assert move_logic.get_move() == 4

def test_move_logic_1st_move_when_2nd_is_corner_space_if_middle_taken(move_logic, board):
    board.mark_space(4, "o")
    assert move_logic.get_move() in [0, 2, 6, 8]

def test_move_logic_prevents_opponent_from_fork_win(move_logic, board):
    board.mark_space(0, "o")
    board.mark_space(4, "x")
    board.mark_space(8, "o")
    assert move_logic.get_move() in [1, 3, 5, 7]

def test_move_logic_prevents_opponent_from_fork_win_side_middle(move_logic, board):
    board.mark_space(0, "o")
    board.mark_space(4, "x")
    board.mark_space(7, "o")
    assert move_logic.get_move() not in [2, 1]

def test_move_logic_ends_game_when_possible(move_logic, board):
    board.mark_space(0, "o")
    board.mark_space(1, "o")
    board.mark_space(7, "x")
    board.mark_space(8, "x")
    assert move_logic.get_move() == 6

def test_move_logic_prevents_opponent_from_fork_win_middle_two_corners(move_logic, board):
    board.mark_space(4, "o")
    board.mark_space(8, "x")
    board.mark_space(0, "o")
    assert move_logic.get_move() in [2, 6]


@pytest.fixture()
def big_board():
    return Board.create_fresh_board(16)
@pytest.fixture()
def move_logic_with_large_board(big_board):
    return MoveLogic("x", big_board)

def test_move_logic_can_make_winning_move_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(0, "x")
    big_board.mark_space(1, "x")
    big_board.mark_space(3, "x")
    assert move_logic_with_large_board.get_move() == 2

def test_move_logic_can_stop_immediate_horizontal_loss_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(4, "o")
    big_board.mark_space(5, "o")
    big_board.mark_space(6, "o")
    assert move_logic_with_large_board.get_move() == 7

def test_move_logic_ends_game_when_possible_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(0, "o")
    big_board.mark_space(1, "o")
    big_board.mark_space(2, "o")
    big_board.mark_space(12, "x")
    big_board.mark_space(13, "x")
    big_board.mark_space(14, "x")
    assert move_logic_with_large_board.get_move() == 15

def test_move_logic_prevents_fork_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(3, "o")
    big_board.mark_space(5, "o")
    big_board.mark_space(6, "o")
    big_board.mark_space(11, "o")
    big_board.mark_space(13, "x")
    big_board.mark_space(14, "x")
    assert move_logic_with_large_board.get_move() == 7

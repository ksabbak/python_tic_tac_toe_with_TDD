import pytest

from tictactoe.app.__init__ import Board, MoveLogic


@pytest.fixture()
def board():
    return Board.create_fresh_board()
@pytest.fixture()
def move_logic(board):
    return MoveLogic(board)

def tests_move_logic_can_move_without_input(move_logic, board):
    assert move_logic.get_move(0) in range(0, 9)

def tests_move_logic_moves_to_empty_spot(move_logic, board):
    for i in range(8):
        board.mark_space(i, 1)
    assert move_logic.get_move(0) == 8

def test_move_logic_can_make_horizontal_winning_move(move_logic, board):
    board.mark_space(0, 0)
    board.mark_space(1, 0)
    assert move_logic.get_move(2) == 2

def test_move_logic_can_make_vertical_winning_move(move_logic, board):
    board.mark_space(0, 0)
    board.mark_space(3, 0)
    assert move_logic.get_move(4) == 6

def test_move_logic_can_make_diagonal_winning_move(move_logic, board):
    board.mark_space(0, 0)
    board.mark_space(8, 2)
    assert move_logic.get_move(4) == 4

def test_move_logic_can_stop_immediate_horizontal_loss0(move_logic, board):
    board.mark_space(3, 0)
    board.mark_space(0, 1)
    board.mark_space(4, 2)
    assert move_logic.get_move(3) == 5

def test_move_logic_can_stop_immediate_horizontal_loss2(move_logic, board):
    board.mark_space(3, 0)
    board.mark_space(2, 1)
    board.mark_space(4, 2)
    assert move_logic.get_move(3) == 5

def test_move_logic_can_stop_immediate_horizontal_loss6(move_logic, board):
    board.mark_space(3, 0)
    board.mark_space(6, 1)
    board.mark_space(4, 2)
    assert move_logic.get_move(3) == 5

def test_move_logic_prevents_opponent_from_fork_win(move_logic, board):
    board.mark_space(0, 0)
    board.mark_space(4, 1)
    board.mark_space(8, 0)
    assert move_logic.get_move(1) in [1, 3, 5, 7]

def test_move_logic_prevents_opponent_from_fork_win_side_middle(move_logic, board):
    board.mark_space(0, 0)
    board.mark_space(4, 1)
    board.mark_space(7, 0)
    assert move_logic.get_move(1) not in [2, 1]

def test_move_logic_ends_game_when_possible(move_logic, board):
    board.mark_space(0, 0)
    board.mark_space(1, 0)
    board.mark_space(7, 1)
    board.mark_space(8, 1)
    assert move_logic.get_move(1) == 6

def test_move_logic_prevents_opponent_from_fork_win_middle_two_corners(move_logic, board):
    board.mark_space(4, 0)
    board.mark_space(8, 1)
    board.mark_space(0, 0)
    assert move_logic.get_move(1) in [2, 6]


@pytest.fixture()
def big_board():
    return Board.create_fresh_board(16)
@pytest.fixture()
def move_logic_with_large_board(big_board):
    return MoveLogic(big_board)

def test_move_logic_can_make_winning_move_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(0, 1)
    big_board.mark_space(1, 1)
    big_board.mark_space(3, 1)
    assert move_logic_with_large_board.get_move(1) == 2

def test_move_logic_can_stop_immediate_horizontal_loss_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(4, 0)
    big_board.mark_space(5, 0)
    big_board.mark_space(6, 0)
    assert move_logic_with_large_board.get_move(1) == 7

def test_move_logic_ends_game_when_possible_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(0, 0)
    big_board.mark_space(1, 0)
    big_board.mark_space(2, 0)
    big_board.mark_space(12, 1)
    big_board.mark_space(13, 1)
    big_board.mark_space(14, 1)
    assert move_logic_with_large_board.get_move(1) == 15

def test_move_logic_prevents_fork_16_space_board(move_logic_with_large_board, big_board):
    big_board.mark_space(3, 0)
    big_board.mark_space(5, 0)
    big_board.mark_space(6, 0)
    big_board.mark_space(11, 0)
    big_board.mark_space(0, 1)
    big_board.mark_space(13, 1)
    big_board.mark_space(14, 1)
    assert move_logic_with_large_board.get_move(1) in [7, 4, 12, 15]

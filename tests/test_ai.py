import pytest

from ..app.__init__ import AI, Player, Board

@pytest.fixture()
def ai():
    return AI("x")
@pytest.fixture()
def board():
    return Board()

def tests_ai_is_a_player():
    assert issubclass(AI, Player)

def tests_ai_can_move_without_input(ai, board):
    print("------ANY MOVE--------")
    assert ai.get_move(board) in range(0, 9)

def tests_ai_moves_to_empty_spot(ai, board):
    for i in range(1, 9):
        board.mark_space(i, "x")
    print("------EMPTY SPOT--------")
    assert ai.get_move(board) == 0

def test_ai_can_make_winning_move(ai, board):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    print("------WINNING MOVE--------")
    assert ai.get_move(board) == 2

def test_ai_can_stop_immediate_loss(ai, board):
    board.mark_space(3, "o")
    board.mark_space(8, "x")
    board.mark_space(4, "o")
    print("------LOSING MOVE--------")
    assert ai.get_move(board) == 5

def test_ai_1st_move_when_1st_is_center(ai, board):
    print("------1st MOVE--------")
    assert ai.get_move(board) == 4

def test_ai_1st_move_when_2nd_is_middle_space_if_open(ai, board):
    board.mark_space(3, "o")
    print("------2nd MOVE--------")
    assert ai.get_move(board) == 4

def test_ai_prevents_opponent_from_fork_win(ai, board):
    board.mark_space(0, "o")
    board.mark_space(4, "x")
    board.mark_space(8, "o")
    assert ai.get_move(board) in [1, 3, 5, 7]

def test_ai_prevents_opponent_from_fork_win_middle(ai, board):
    board.mark_space(0, "o")
    board.mark_space(4, "x")
    board.mark_space(7, "o")
    assert ai.get_move(board) not in [2, 1]

def test_ai_can_determine_opponent_marker(ai, board):
    board.mark_space(0, "o")
    assert ai._deduce_opponent_marker(board) == "o"

def test_ai_knows_spaces(ai, board):
    board.mark_space(0, "o")
    board.mark_space(1, "o")
    board.mark_space(2, "o")
    board.mark_space(3, "o")
    board.mark_space(4, "x")
    board.mark_space(5, "x")
    board.mark_space(6, "x")
    board.mark_space(7, "o")
    assert ai._current_spaces(board, "o") == 5
    assert ai._current_spaces(board, "x") == 3

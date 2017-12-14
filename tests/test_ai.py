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
    assert ai.get_move(board) in range(0, 9)

def tests_ai_moves_to_empty_spot(ai, board):
    for i in range(1, 9):
        board.mark_space(i, "x")
    assert ai.get_move(board) == 0

def test_ai_can_make_winning_move(ai, board):
    board.mark_space(0, "x")
    board.mark_space(1, "x")
    assert ai.get_move(board) == 2

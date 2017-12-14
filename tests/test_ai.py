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

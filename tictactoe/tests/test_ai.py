import pytest

from tictactoe.app.__init__ import AI, Player, Board

@pytest.fixture()
def board():
    return Board.create_fresh_board()
@pytest.fixture()
def ai(board):
    return AI()

def tests_ai_is_a_player():
    assert issubclass(AI, Player)

def test_player_is_ai(ai):
    assert ai.is_ai() is True

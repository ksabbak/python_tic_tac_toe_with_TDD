import pytest

from tictactoe.app.__init__ import AI, Player, Board

@pytest.fixture()
def board():
    return Board.create_fresh_board()
@pytest.fixture()
def ai(board):
    return AI("x")

def tests_ai_is_a_player():
    assert issubclass(AI, Player)

def test_player_is_ai(ai):
    assert ai.is_ai() is True

def test_ai_player_has_move_log(ai):
    assert ai.moves == []

def test_ai_player_logs_moves(ai, board):
    move = ai.make_move(board, None)
    move_2 = ai.make_move(board, None)
    assert ai.moves == [move, move_2]

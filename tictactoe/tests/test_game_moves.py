import pytest

from tictactoe.app.models.game_moves import GameMoves

@pytest.fixture()
def game_moves():
    return GameMoves()

def test_game_moves_can_append_moves(game_moves):
    game_moves.append(9)
    assert len(game_moves) == 1
    assert game_moves.moves == (9, )

def test_game_moves_undoes_full_turn(game_moves):
    game_moves.append(1)
    game_moves.append(3)
    game_moves.append(4)
    game_moves.undo(["player1", "player2"])
    assert len(game_moves) == 1
    assert game_moves.moves == (1, )

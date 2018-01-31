import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.__init__ import Player, HumanPlayer, Board


def xtest_players_have_markers():
    assert Player().marker is not None
    assert Player().marker.strip("'\033[0m'") == "!"

def test_player_undo_removes_last_move():
    player = Player()
    player.moves = [1, 2, 3]
    player.undo()
    assert player.moves == [1, 2]

def test_player_undo_to_empty_does_not_break_everything():
    player = Player()
    player.undo()
    assert player.moves == []

@pytest.fixture()
def human_playerx():
    return HumanPlayer()

def test_human_player_is_not_ai(human_playerx):
    assert human_playerx.is_ai() is False

def test_human_player_has_move_log(human_playerx):
    assert human_playerx.moves == []

def test_human_player_logs_moves(human_playerx):
    board = Board.create_fresh_board()
    human_playerx.make_move(board, 8, 0)
    human_playerx.make_move(board, 0, 2)
    human_playerx.make_move(board, 4, 4)
    assert human_playerx.moves == [8, 0, 4]

def xtest_get_move(human_playerx):
    with unittest.mock.patch('builtins.input', return_value='7'):
        assert human_playerx.get_move() == 7

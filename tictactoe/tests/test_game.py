import sys
import pytest
import io

from tictactoe.app.__init__ import Game

@pytest.fixture()
def game():
    return Game()

# GENERAL
def test_there_is_a_game(game):
    assert game is not None

def test_game_is_marked_over_when_board_is_filled(game):
    i = 0
    while i < len(game.board.spaces):
        game.board.mark_space(i, "X")
        i += 1
    assert game.is_over() is True

def test_game_is_marked_over_when_there_is_a_winner(game):
    game.board.mark_space(0, 1)
    game.board.mark_space(3, 3)
    game.board.mark_space(6, 5)
    assert game.is_over() is True

def test_game_is_not_marked_over_when_not_over(game):
    game.board.mark_space(0, 0)
    game.board.mark_space(3, 1)
    game.board.mark_space(6, 2)
    assert game.is_over() is False

def test_undo_removes_last_move_from_both_players(game):
    game.players[0].make_move(game.board, 4, 0)
    game.players[1].make_move(game.board, 5, 1)
    game.players[0].make_move(game.board, 0, 2)
    game.undo_turn()
    assert len(game.players[0].moves) == 1
    assert len(game.players[1].moves) == 0

def test_undo_does_not_cause_lost_turn(game):
    current_player = game.current_player
    game.undo_turn()
    game.end_turn()
    assert game.current_player == current_player

# BOARD
def test_game_has_board(game):
    assert game.board is not None

#PLAYERS
def test_game_has_two_players(game):
    assert len(game.players) == 2

def xtest_player_one_has_marker_x(game):
    assert game.players[0].marker.strip('\033[0m') == "x"

def xtest_player_two_has_marker_o(game):
    assert game.players[1].marker.strip('\033[0m') == "o"

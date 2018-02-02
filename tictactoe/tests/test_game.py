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
    assert len(game.board.empty_spaces()) == 9
    for i in range(0, 4):
        game.start_turn(i)
        game.end_turn()
    assert len(game.board.empty_spaces()) == 5
    game.undo_turn()
    game.end_turn()
    assert len(game.board.empty_spaces()) == 7

def test_undo_does_not_cause_lost_turn(game):
    current_player = game.current_player
    for i in range(0, 4):
        game.start_turn(i)
        game.end_turn()
    game.undo_turn()
    game.end_turn()
    assert current_player == game.current_player

def test_undo_does_not_repeat_turn(game):
    for i in range(0, 4):
        game.start_turn(i)
        game.end_turn()
    game.undo_turn()
    game.end_turn()
    assert game.turn not in game.board.spaces

def test_winner(game):
    assert game.winner() == None
    game.board.mark_space(3, 0)
    game.board.mark_space(4, 2)
    game.board.mark_space(5, 4)
    assert game.winner() == game.players[0]

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

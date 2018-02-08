import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.game_builder import GameBuilder

@pytest.fixture()
def game_builder():
    return GameBuilder()

def test_game_builder_choses_proper_game(game_builder):
    pvp = '1'
    with unittest.mock.patch('builtins.input', return_value=pvp):
        game = game_builder.impliment_game_choice()
        assert game.players[0].is_ai() is False
        assert game.players[1].is_ai() is False
    cvc = '3'
    with unittest.mock.patch('builtins.input', return_value=cvc):
        game = game_builder.impliment_game_choice()
        assert game.players[0].is_ai() is True
        assert game.players[1].is_ai() is True

def test_game_builder_choses_proper_player_order_for_mixed_game(game_builder):
    mixed_game = '2'
    going_first = 'yes'
    with unittest.mock.patch('builtins.input', side_effect=[mixed_game, going_first]):
        game = game_builder.impliment_game_choice()
        assert game.players[0].is_ai() is False
        assert game.players[1].is_ai() is True
    not_going_first = 'no'
    with unittest.mock.patch('builtins.input', side_effect=[mixed_game, not_going_first]):
        game = game_builder.impliment_game_choice()
        assert game.players[0].is_ai() is True
        assert game.players[1].is_ai() is False

def test_game_builder_can_return_appropriate_board_choice(game_builder):
    three_by_three = "1"
    with unittest.mock.patch('builtins.input', return_value=three_by_three):
        board_choice = game_builder.make_board_choice()
        assert board_choice == 9
    four_by_four = "2"
    with unittest.mock.patch('builtins.input', return_value=four_by_four):
        board_choice = game_builder.make_board_choice()
        assert board_choice == 16


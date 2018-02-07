import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.game_builder import GameBuilder


def test_game_builder_choses_proper_game():
    game_builder = GameBuilder()
    with unittest.mock.patch('builtins.input', return_value='1'):
        game = game_builder.impliment_game_choice(9)
        assert game.players[0].is_ai() is False
        assert game.players[1].is_ai() is False
    with unittest.mock.patch('builtins.input', return_value='3'):
        game = game_builder.impliment_game_choice(9)
        assert game.players[0].is_ai() is True
        assert game.players[1].is_ai() is True

def test_game_builder_choses_proper_player_order_for_mixed_game():
    game_builder = GameBuilder()
    with unittest.mock.patch('builtins.input', side_effect=['2', 'yes']):
        game = game_builder.impliment_game_choice(9)
        assert game.players[0].is_ai() is False
        assert game.players[1].is_ai() is True
    with unittest.mock.patch('builtins.input', side_effect=['2', 'no']):
        game = game_builder.impliment_game_choice(9)
        assert game.players[0].is_ai() is True
        assert game.players[1].is_ai() is False

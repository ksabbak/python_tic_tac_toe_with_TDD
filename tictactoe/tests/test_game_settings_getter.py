import pytest
import unittest

from tictactoe.app.game_settings_getter import GameSettingsGetter
from tictactoe.tests.helpers import mock_get_game_input

@pytest.fixture()
def game_settings_getter():
    return GameSettingsGetter()

def test_game_settings_getter_choses_proper_game_player_vs_player(game_settings_getter):
    pvp = '1'
    board_choice = 9
    with unittest.mock.patch('builtins.input', return_value=pvp):
        game = game_settings_getter.impliment_game_choice(board_choice)
        assert game.players[0].is_ai() is False
        assert game.players[1].is_ai() is False

def test_game_settings_getter_choses_proper_game_player_vs_comp(game_settings_getter):
    pvc = '2'
    board_choice = 9
    with unittest.mock.patch('builtins.input', return_value=pvc):
        game = game_settings_getter.impliment_game_choice(board_choice)
        assert game.players[0].is_ai() is False
        assert game.players[1].is_ai() is True

def test_game_settings_getter_choses_proper_game_comp_vs_player(game_settings_getter):
    cvp = '3'
    board_choice = 9
    with unittest.mock.patch('builtins.input', return_value=cvp):
        game = game_settings_getter.impliment_game_choice(board_choice)
        assert game.players[0].is_ai() is True
        assert game.players[1].is_ai() is False

def test_game_settings_getter_choses_proper_game_comp_vs_comp(game_settings_getter):
    cvc = '4'
    board_choice = 9
    with unittest.mock.patch('builtins.input', return_value=cvc):
        game = game_settings_getter.impliment_game_choice(board_choice)
        assert game.players[0].is_ai() is True
        assert game.players[1].is_ai() is True

def xtest_game_settings_getter_choice_with_mock():
    input_one = mock_get_game_input("1")
    game_settings_getter = GameSettingsGetter(game_type_input=input_one)
    game = game_settings_getter.impliment_game_choice()
    assert game.players[0].is_ai() is False
    assert game.players[1].is_ai() is False


def test_game_settings_getter_can_return_appropriate_board_choice(game_settings_getter):
    three_by_three = "1"
    with unittest.mock.patch('builtins.input', return_value=three_by_three):
        board_choice = game_settings_getter.make_board_choice()
        assert board_choice == 9
    four_by_four = "2"
    with unittest.mock.patch('builtins.input', return_value=four_by_four):
        board_choice = game_settings_getter.make_board_choice()
        assert board_choice == 16


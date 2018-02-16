import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.validator import Validator
from tictactoe.tests.helpers import mock_for_validator

def test_validator_requires_valid_input_for_acceptable_game_type():
    mock = mock_for_validator(['100', '1'])
    valid_input = Validator().handle_input(mock, "game_type")
    assert valid_input is not '100'
    assert valid_input is '1'

def test_validator_requires_valid_input_for_acceptable_board_type():
    mock = mock_for_validator(['100', '1'])
    valid_input = Validator().handle_input(mock, "board_type")
    assert valid_input is not '100'
    assert valid_input is '1'

def test_validator_requires_valid_input_for_acceptable_color_name():
    mock = mock_for_validator(['reed', 'red'])
    valid_input = Validator().handle_input(mock, "color_name")
    assert valid_input is not 'reed'
    assert valid_input is 'red'

def test_validator_is_case_insensitve_for_color_name():
    mock = mock_for_validator(['GreEn'])
    valid_input = Validator().handle_input(mock, "color_name")
    assert valid_input is 'GreEn'

def test_validator_accepts_none_color():
    mock = mock_for_validator(['None'])
    valid_input = Validator().handle_input(mock, "color_name")
    assert valid_input is 'None'

def test_validator_requires_valid_marker_input():
    mock = mock_for_validator(['reed', ' ', '  ', 'x'])
    valid_input = Validator().handle_input(mock, "marker_input")
    assert valid_input is not 'reed'
    assert valid_input is not ' '
    assert valid_input is not '  '
    assert valid_input is 'x'

def test_validator_no_matches_returns_true_if_list_has_no_matches():
    lst = [1, 2, 3, 4, 5]
    no_matches = Validator().no_matches(lst)
    assert no_matches == True

def test_validator_no_matches_returns_none_if_list_has_matches():
    lst = [1, 2, 3, 4, 1]
    no_matches = Validator().no_matches(lst)
    assert no_matches == None

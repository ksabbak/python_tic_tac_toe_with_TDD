import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.move_coordinates_validator import MoveCoordinatesValidator
from tictactoe.app.__init__ import Board
from tictactoe.tests.helpers import mock_for_validator

@pytest.fixture()
def board():
    board = Board.create_fresh_board()
    return board

def test_move_coord_validator_requires_valid_input_for_move_input(board):
    mock = mock_for_validator(['100', '1A'])
    valid_input = MoveCoordinatesValidator(board).handle_input(mock, "move_input")
    assert valid_input is not '100'
    assert valid_input is '1A'

def test_move_coord_validator_does_not_care_about_coordinate_order(board):
    mock = mock_for_validator(['3C'])
    valid_input = MoveCoordinatesValidator(board).handle_input(mock, "move_input")
    assert valid_input is '3C'
    mock = mock_for_validator(['C3'])
    valid_input = MoveCoordinatesValidator(board).handle_input(mock, "move_input")
    assert valid_input is 'C3'

def test_move_coord_validator_does_not_care_about_case(board):
    mock = mock_for_validator(['2b'])
    valid_input = MoveCoordinatesValidator(board).handle_input(mock, "move_input")
    assert valid_input is '2b'
    mock = mock_for_validator(['B2'])
    valid_input = MoveCoordinatesValidator(board).handle_input(mock, "move_input")
    assert valid_input is 'B2'

def test_move_coord_validator_does_not_allow_move_on_taken_spot(board):
    board.mark_space(0, 0)
    mock = mock_for_validator(['A1', 'B2'])
    valid_input = MoveCoordinatesValidator(board).handle_input(mock, "move_input")
    assert valid_input is not 'A1'
    assert valid_input is 'B2'



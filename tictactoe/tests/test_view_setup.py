import pytest
import unittest
from unittest.mock import patch #This mock is used

from tictactoe.app.view_setup import ViewSetup

def test_view_setup_requires_unique_markers():
    marker1 = "x"
    color1 = "red"
    marker2 = "o"
    color2 = "green"
    irrelevant_to_this_test_board_color = 'green'
    with unittest.mock.patch('builtins.input', side_effect=[marker1, color1, marker1, color1, marker2, color2, irrelevant_to_this_test_board_color ]):
        view_setup = ViewSetup.setup_view()
        assert len(view_setup.player_markers) == 2
        assert view_setup.player_markers[0] != view_setup.player_markers[1]


def test_view_setup_works_with_unique_markers():
    marker1 = 'x'
    marker2 = 'o'
    color = 'red'
    with unittest.mock.patch('builtins.input', side_effect=[marker1, color, marker2, color, color]):
        view_setup = ViewSetup.setup_view()
        assert len(view_setup.player_markers) == 2

def test_view_setup_works_with_unique_colors():
    marker = 'x'
    color1 = 'red'
    color2 = 'none'
    irrelevant_to_this_test_board_color = color1
    with unittest.mock.patch('builtins.input', side_effect=[marker, color1, marker, color2, irrelevant_to_this_test_board_color]):
        view_setup = ViewSetup.setup_view()
        assert len(view_setup.player_markers) == 2


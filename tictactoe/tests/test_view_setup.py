import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.view_setup import ViewSetup

def test_view_setup_returns_board_decorator():
    with unittest.mock.patch('builtins.input', side_effect=['x', 'red', 'o', 'blue', 'green' ]):
        assert ViewSetup().get_markers_and_colors("one", "two").__class__.__name__ is 'BoardDecorator'

def test_view_setup_requires_unique_markers():
    with unittest.mock.patch('builtins.input', side_effect=['x', 'red', 'x', 'red', 'o', 'blue' ]):
        view_setup = ViewSetup.setup_view()
        assert len(view_setup.players) == 2
        assert view_setup.players[0] != view_setup.players[1]


def test_view_setup_works_with_unique_markers():
    with unittest.mock.patch('builtins.input', side_effect=['x', 'red', 'o', 'blue']):
        view_setup = ViewSetup.setup_view()
        assert len(view_setup.players) == 2


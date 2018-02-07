import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.view_setup import ViewSetup

def test_view_setup_returns_board_decorator():
    with unittest.mock.patch('builtins.input', side_effect=['x', 'red', 'o', 'blue', 'green' ]):
        assert ViewSetup().get_markers_and_colors("one", "two").__class__.__name__ is 'BoardDecorator'

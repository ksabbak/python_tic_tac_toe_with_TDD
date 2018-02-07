import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.validator import Validator


def xtest_controller_choses_proper_game():
    with unittest.mock.patch('builtins.input', return_value='1'):
        assert Controller().run() in "Human vs. Human!"
    with unittest.mock.patch('builtins.input', return_value='2'):
        assert Controller().run() in "Human vs. Computer!"
    with unittest.mock.patch('builtins.input', return_value='3'):
        assert Controller().run() in "Computer vs. Computer!"

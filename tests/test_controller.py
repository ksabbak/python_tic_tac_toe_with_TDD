import pytest
import unittest
from unittest.mock import patch

from ..app.controller import Controller

def tests_controller_can_be_called():
    controller = Controller()
    assert controller.run

def xtest_controller_choses_proper_game():
    with unittest.mock.patch('builtins.input', return_value='1'):
        assert Controller().run() in "Human vs. Human!"
    with unittest.mock.patch('builtins.input', return_value='2'):
        assert Controller().run() in "Human vs. Computer!"
    with unittest.mock.patch('builtins.input', return_value='3'):
        assert Controller().run() in "Computer vs. Computer!"

def test_coordinate_to_number():
    controller = Controller()
    assert controller._coordinate_to_number("a1") == 0
    assert controller._coordinate_to_number("2B") == 4

def test_number_to_coordinate():
    controller = Controller()
    assert controller._number_to_coordinate(5) == "B3"
    assert controller._number_to_coordinate(8) == "C3"

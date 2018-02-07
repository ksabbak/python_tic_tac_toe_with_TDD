import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.controller import Controller

def tests_controller_can_be_called():
    controller = Controller()
    assert controller.run

def test_coordinate_to_number():
    controller = Controller()
    assert controller._coordinate_to_number("a1") == 0
    assert controller._coordinate_to_number("2B") == 4

def test_number_to_coordinate():
    controller = Controller()
    assert controller._number_to_coordinate(5) == "B3"
    assert controller._number_to_coordinate(8) == "C3"

def test_affirmation():
    assert Controller()._affirmative("Okay!") is True
    assert Controller()._affirmative("No thanks") is False

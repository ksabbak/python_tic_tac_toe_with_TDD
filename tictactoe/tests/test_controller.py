import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.controller import Controller

def tests_controller_can_be_called():
    controller = Controller()
    assert controller.run

def test_number_to_coordinate():
    controller = Controller()
    assert controller._number_to_coordinate(5) == "B3"
    assert controller._number_to_coordinate(8) == "C3"


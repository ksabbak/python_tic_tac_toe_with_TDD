import pytest
import unittest
from unittest.mock import patch

from tictactoe.app.controller import Controller

def tests_controller_can_be_called():
    controller = Controller()
    assert controller.run




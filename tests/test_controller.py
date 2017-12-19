import pytest

from ..app.controller import Controller

def tests_controller_can_be_called():
    controller = Controller()
    assert controller.run()

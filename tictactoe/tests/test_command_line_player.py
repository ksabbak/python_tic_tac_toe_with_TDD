import pytest

from tictactoe.app.command_line_player import CommandLinePlayer
from tictactoe.app.command_line_views.coordinate import Coordinate
from tictactoe.app.__init__ import Game

class MockMoveCoordinatesValidator:
    def __init__(self, *args):
        pass

    def handle_input(self, funciton, *args):
        return(function())


class MockBoardDecorator:
    def get_marker_for_current_turn(self, *args):
        pass

@pytest.fixture()
def pvp():
    game = Game.pvp(9)
    arguments = {
            board_decorator: MockBoardDecorator(),
            coordinates: Coordinate(3),
            game: game,
            move_coordinates_validator: MockMoveCoordinatesValidator,
            }
    CommandLinePlayer(**arguments)

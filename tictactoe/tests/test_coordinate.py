import pytest

from tictactoe.app.command_line_views.coordinate import Coordinate


def test_coordinate_can_build_coordinates_3x3():
    coordinate = Coordinate(3)
    assert coordinate.coordinates == ['A1', 'A2', 'A3',
                                 'B1', 'B2', 'B3',
                                 'C1', 'C2', 'C3'
                                 ]


def test_coordinate_can_build_coordinates_4x4():
    coordinate = Coordinate(4)
    assert coordinate.coordinates == ['A1', 'A2', 'A3', 'A4',
                                     'B1', 'B2', 'B3', 'B4',
                                     'C1', 'C2', 'C3', 'C4',
                                     'D1', 'D2', 'D3', 'D4'
                                     ]

def test_coordinate_number_to_coordinate_3x3():
    coordinate = Coordinate(3)
    assert coordinate.number_to_coordinate(5) == "B3"
    assert coordinate.number_to_coordinate(8) == "C3"

def test_coordinate_number_to_coordinate_4x4():
    coordinate = Coordinate(4)
    assert coordinate.number_to_coordinate(5) == "B2"
    assert coordinate.number_to_coordinate(8) == "C1"
    assert coordinate.number_to_coordinate(15) == "D4"

def test_coordinate_coordinate_to_number_3x3():
    coordinate = Coordinate(3)
    assert coordinate.coordinate_to_number("B3") == 5
    assert coordinate.coordinate_to_number("C3") == 8

def test_coordinate_coordinate_to_number_4x4():
    coordinate = Coordinate(4)
    assert coordinate.coordinate_to_number("B2") == 5
    assert coordinate.coordinate_to_number("C1") == 8
    assert coordinate.coordinate_to_number("D4") == 15

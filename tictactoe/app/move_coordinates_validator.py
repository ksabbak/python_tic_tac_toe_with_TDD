from .validator import Validator
from .exceptions import TicTacToeInputException
from .coordinate import Coordinate

class MoveCoordinatesValidator(Validator):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.coordinate = Coordinate(board.side_length())
        self.ACCEPTABLE_FUNCTIONS.update({
                'move_input' : '_acceptable_move_input'
                })

    def _acceptable_move_input(self, move_input):
        if move_input == "undo": return
        move_input = self.coordinate.coordinate_to_number(move_input)
        if move_input is None:
            raise TicTacToeInputException("Sorry, I can't find that coordinate.")
        if move_input not in self.board.empty_spaces():
            raise TicTacToeInputException("Sorry, looks like that spot is taken.")

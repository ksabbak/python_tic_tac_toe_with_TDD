from .validator import Validator

class MoveCoordinatesValidator(Validator):
    def __init__(self, board):
        self.board = board
        self.ACCEPTABLE_FUNCTIONS = super().ACCEPTABLE_FUNCTIONS + {
                'move_input' : '_acceptable_move_input'
                }

    def _acceptable_move_input(self, move_input):
        if move_input == "undo": return
        move_input = self._format_move_input(move_input)
        move_input = self._coordinate_to_number(move_input)
        if move_input is None:
            raise TicTacToeInputException("Sorry, I can't find that coordinate.")
        if move_input not in self.board.empty_spaces():
            raise TicTacToeInputException("Sorry, looks like that spot is taken.")

    def _format_move_input(self, move):
        coord_list = list(move.upper())
        coord_list.sort()
        coord_list.reverse()
        return "".join(coord_list)

    def _coordinate_to_number(self, move):
        move = self._format_move_input(move)
        if move in self.board.coordinates:
            return self.board.coordinates.index(move)

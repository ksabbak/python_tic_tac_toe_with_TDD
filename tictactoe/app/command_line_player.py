from .validator import Validator
from .move_coordinates_validator import MoveCoordinatesValidator
from .command_line_views.view_getter import ViewGetter
from .command_line_views.view_printer import ViewPrinter


class CommandLinePlayer:
    def __init__(self, board_decorator, coordinates, game, view_printer=ViewPrinter, move_coordinates_validator=MoveCoordinatesValidator):
        self.coordinates = coordinates
        self.board_decorator = board_decorator
        self.game = game
        self.view_printer = view_printer
        self.move_coordinates_validator = move_coordinates_validator(self.game.board)

    def play(self):
        self.view_printer.print_new_turn(self.game.board, self.board_decorator, self.game.last_move)
        while not self.game.is_over():
            if self.game.current_player.is_ai():
                self._ai_player_turn()
            else:
                self._human_player_turn()
            self.game.end_turn()

    def _human_player_turn(self):
        move = self.move_coordinates_validator.handle_input(ViewGetter.get_player_move, "move_input", [self.board_decorator.get_marker_for_current_turn(self.game.turn)])
        if move == "undo":
            self.game.undo_turn()
        else:
            self.game.start_turn(self.coordinates.coordinate_to_number(move))
        move = self.game.last_move
        self.view_printer.print_humanplayer_update(self.game.board, self.board_decorator, self.coordinates.number_to_coordinate(move), self.game.turn, self.game.players)

    def _ai_player_turn(self):
        self.view_printer.print_ai_thinking()
        move = self.game.start_turn()
        self.view_printer.print_ai_update(self.game.board, self.board_decorator, self.coordinates.number_to_coordinate(move), self.game.turn)

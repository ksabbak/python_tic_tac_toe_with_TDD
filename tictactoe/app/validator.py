from .command_line_views.view_printer import print_sorry


class Validator:
    def __init__(self):
        pass

    # def _acceptable_marker_input(self, marker_input):
    #     if len(marker_input) != 1 or marker_input == " ":
    #         return "marker length"

    # def _acceptable_game_type_input(self, game_type_input):
    #     if game_type_input not in ["1", "2", "3"]:
    #         return "game type"

    # def _acceptable_board_type_input(self, board_type_input):
    #     if board_type_input not in ["1", "2"]:
    #         return "board type"

    # def _acceptable_color_input(self, color_input):
    #     color_input = color_input.lower().strip(punctuation)
    #     if color_input == "none": return None
    #     for color in self._colors():
    #         if color_input == color.lower(): return None
    #     return "color"

    # def _acceptable_move_input(self, move_input):
    #     if move_input == "undo": return
    #     move_input = self._format_move_input(move_input)
    #     move_input = self._coordinate_to_number(move_input)
    #     if move_input is None:
    #         return "no coord"
    #     if move_input not in self.game.board.empty_spaces():
    #         return "taken"

    @classmethod
    def handle_input(cls, input_getter, input_parser, arguments=[]):
        user_input = None
        while user_input is None:
            user_input = input_getter(*arguments)
            unacceptable_input = input_parser(user_input)
            if unacceptable_input:
                user_input = None
                print_sorry(unacceptable_input)
            else:
                return user_input

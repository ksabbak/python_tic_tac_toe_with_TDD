from string import punctuation
from .command_line_views.view_printer import ViewPrinter
from .command_line_views.colorist import Colorist
from .command_line_views.view_config import BOARD_CHOICE, GAME_CHOICE
from .exceptions import TicTacToeInputException

class Validator:
    def __init__(self):
        self.ACCEPTABLE_FUNCTIONS = {
            'board_type' : '_acceptable_board_type_input',
            'color_name' : '_acceptable_color_input',
            'game_type' : '_acceptable_game_type_input',
            'marker_input' : '_acceptable_marker_input',
        }

    def handle_input(self, input_getter, input_type, arguments=[]):
        user_input = None
        while user_input is None:
            user_input = input_getter(*arguments)
            input_checker = getattr(self, self.ACCEPTABLE_FUNCTIONS[input_type])
            if not self._check_if_input_is_valid(input_checker, user_input):
                user_input = None
        return user_input

    def no_matches(self, might_have_matches):
        checker = getattr(self, '_no_match_checker')
        return self._check_if_input_is_valid(checker, might_have_matches)


    def _check_if_input_is_valid(self, checker, input):
        try:
            checker(input)
        except TicTacToeInputException as error:
            ViewPrinter.print_error(error)
        else:
            return True

    def _no_match_checker(self, might_have_matches):
        reduced_set = set(might_have_matches)
        if len(reduced_set) != len(might_have_matches):
            raise TicTacToeInputException("Sorry, markers have to differ in shape or color from other players' markers.")

    def _acceptable_game_type_input(self, game_type_input):
        if game_type_input not in GAME_CHOICE.keys():
            raise TicTacToeInputException("Please enter the numeral 1, 2, 3, or 4:")

    def _acceptable_board_type_input(self, board_type_input):
        if board_type_input not in BOARD_CHOICE.keys():
            raise TicTacToeInputException("Please enter the numeral 1 or 2:")

    def _acceptable_color_input(self, color_input):
        color_input = color_input.lower().strip(punctuation)
        if color_input == "none": return None
        for color in Colorist.color_names():
            if color_input == color.lower(): return None
        raise TicTacToeInputException(self._color_exception())

    def _color_exception(self):
        return (("I didn't quite understand that. Try one of these: ") + Colorist.color_option_string() + ("or 'none' for default"))

    def _acceptable_marker_input(self, marker_input):
        if len(marker_input) != 1 or marker_input == " ":
            raise TicTacToeInputException("Sorry, your marker can only be one character.")

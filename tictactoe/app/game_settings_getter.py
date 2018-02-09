from string import punctuation

from .__init__ import Game
from .validator import Validator
from .command_line_views.view_getters import get_game_type_input, get_who_first
from .command_line_views.view_printer import print_who_first
from .command_line_views.view_config import BOARD_CHOICE, GAME_CHOICE

class GameSettingsGetter:
    def __init__(self, choice=9, game_type_input=get_game_type_input):
        self.board_choice = choice
        self.game_type_input = game_type_input

    def build_game(self):
        self.make_board_choice()
        return self.impliment_game_choice()

    def make_board_choice(self):
        board_choice = Validator.handle_input(self.game_type_input, 'board_type')
        self.board_choice = BOARD_CHOICE[board_choice]
        return self.board_choice

    def impliment_game_choice(self):
        game_choice = Validator.handle_input(self.game_type_input, 'game_type')
        game_choice = getattr(Game, GAME_CHOICE[game_choice])
        return game_choice(self.board_choice)



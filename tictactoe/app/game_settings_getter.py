from .__init__ import Game
from .validator import Validator
from .command_line_views.view_getters import get_game_type_input
from .command_line_views.view_config import BOARD_CHOICE, GAME_CHOICE

class GameSettingsGetter:
    def __init__(self, game_type_input=get_game_type_input):
        self.game_type_input = game_type_input

    def make_board_choice(self):
        board_choice = Validator().handle_input(self.game_type_input, 'board_type')
        board_choice = BOARD_CHOICE[board_choice]
        return board_choice

    def impliment_game_choice(self, board_choice):
        game_choice = Validator().handle_input(self.game_type_input, 'game_type')
        game_choice = getattr(Game, GAME_CHOICE[game_choice])
        return game_choice(board_choice)



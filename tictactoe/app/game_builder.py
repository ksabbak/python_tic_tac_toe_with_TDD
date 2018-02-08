from string import punctuation

from .__init__ import Game
from .validator import Validator
from .command_line_views.view_getters import get_game_type_input, get_who_first
from .command_line_views.view_printer import print_who_first
from .command_line_views.view_config import BOARD_CHOICE, GAME_CHOICE

class GameBuilder:
    def __init__(self, choice=9, game_type_input=get_game_type_input):
        self.board_choice = choice
        self.game_type_input = game_type_input

    def build_game(self):
        self.make_board_choice()
        return self.impliment_game_choice()

    def make_board_choice(self):
        board_choice = Validator.handle_input(self.game_type_input, self._acceptable_board_type_input)
        self.board_choice = BOARD_CHOICE[board_choice]
        return self.board_choice

    def impliment_game_choice(self):
        game_choice = Validator.handle_input(self.game_type_input, self._acceptable_game_type_input)
        game_choice = getattr(Game, GAME_CHOICE[game_choice])
        return game_choice(self.board_choice)


    def _get_first_player(self):
        player_first = self._affirmative(get_who_first())
        print_who_first(player_first)
        return player_first

    def _mixed_game(self, player_first):
        if player_first:
            return Game.pvc(self.board_choice)
        else:
            return Game.cvp(self.board_choice)

    def _acceptable_game_type_input(self, game_type_input):
        if game_type_input not in ["1", "2", "3", "4"]:
            return "game type"

    def _acceptable_board_type_input(self, board_type_input):
        if board_type_input not in ["1", "2"]:
            return "board type"

    def _affirmative(self, response):
        response = response.lower().strip(punctuation)
        return (response != "n") and (response in "yes yeah definitely affirmative okay yup sure true")

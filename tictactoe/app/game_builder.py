from string import punctuation

from .__init__ import Game
from .validator import Validator
from .command_line_views.view_getters import get_game_type_input, get_who_first
from .command_line_views.view_printer import print_who_first

class GameBuilder:
    def __init__(self, choice=9):
        self.board_choice = choice

    def build_game(self):
        self.make_board_choice()
        return self.impliment_game_choice()

    def make_board_choice(self):
        board_choice = Validator.handle_input(get_game_type_input, self._acceptable_board_type_input)
        if board_choice in "1":
            self.board_choice = 9
        else:
            self.board_choice = 16
        return self.board_choice

    def impliment_game_choice(self):
        game_choice = Validator.handle_input(get_game_type_input, self._acceptable_game_type_input)
        if game_choice in "1":
            return Game.pvp(self.board_choice)
        elif game_choice in "2":
            return self._mixed_game(self._get_first_player())
        elif game_choice in "3":
            return Game.cvc(self.board_choice)


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
        if game_type_input not in ["1", "2", "3"]:
            return "game type"

    def _acceptable_board_type_input(self, board_type_input):
        if board_type_input not in ["1", "2"]:
            return "board type"

    def _affirmative(self, response):
        response = response.lower().strip(punctuation)
        return (response != "n") and (response in "yes yeah definitely affirmative okay yup sure true")

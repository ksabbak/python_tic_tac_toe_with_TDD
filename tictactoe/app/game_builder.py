from string import punctuation

from .__init__ import Game
from .validator import Validator
from .command_line_views.view_getters import get_game_type_input, get_who_first
from .command_line_views.view_printer import print_who_first

class GameBuilder:

    # TODO: Integrate this into the game builder somehow
    def _make_board_choice(self):
        board_choice = Validator.handle_input(get_game_type_input, self._acceptable_board_type_input)
        if board_choice in "1":
            board_choice = 9
        else:
            board_choice = 16
        return board_choice

    def impliment_game_choice(self, board_choice):
        game_choice = Validator.handle_input(get_game_type_input, self._acceptable_game_type_input)
        if game_choice in "1":
            return Game.pvp(board_choice)
        elif game_choice in "2":
            return self._mixed_game(self._get_first_player(), board_choice)
        elif game_choice in "3":
            return Game.cvc(board_choice)


    def _get_first_player(self):
        player_first = self._affirmative(get_who_first())
        print_who_first(player_first)
        return player_first

    def _mixed_game(self, player_first, board_choice):
        if player_first:
            return Game.pvc(board_choice)
        else:
            return Game.cvp(board_choice)

    def _acceptable_game_type_input(self, game_type_input):
        if game_type_input not in ["1", "2", "3"]:
            return "game type"

    def _affirmative(self, response):
        response = response.lower().strip(punctuation)
        return (response != "n") and (response in "yes yeah definitely affirmative okay yup sure true")

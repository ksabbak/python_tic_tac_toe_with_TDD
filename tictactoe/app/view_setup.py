from string import punctuation

from .validator import Validator
from .command_line_views.board_decorator import BoardDecorator
from .command_line_views.colorist import Colorist
from .command_line_views.view_getters import get_color, get_marker
from .command_line_views.view_printer import print_who_first

class ViewSetup:
    def __init__(self):
        self.first_marker = None
        self.second_marker = None
        self.color1 = None
        self.color2 = None
        self.board_color = None
        self.players = []

    def _set_up_players(self, players):
        for player in players:
            self._add_player(player)

    def _add_player(self, player):
        successful = False
        while not successful:
            colored_marker = self._get_colored_marker(player)
            potential_markers = self.players + [colored_marker]
            if Validator.no_matches(potential_markers):
                self.players.append(colored_marker)
                successful = True


    def get_markers_and_colors(self, player1, player2):
        while self._markers_match() or self._markers_need_filling():
            self.first_marker = Validator.handle_input(get_marker, "marker_input", [player1])
            self.color1 = Validator.handle_input(get_color, "color_name", [self.first_marker])
            self.second_marker = Validator.handle_input(get_marker, "marker_input", [player2])
            self.color2 = Validator.handle_input(get_color, "color_name", [self.second_marker])
            if self._markers_match() or self._markers_need_filling():
                # TODO: fix this - should be part of the validator
                print_sorry("match marker")
        self.board_color = Validator.handle_input(get_color, "color_name", ["the board"])

        board_decorator = BoardDecorator([self.first_marker, self.second_marker], [self.color1, self.color2], self.board_color)

        return board_decorator

    def _get_colored_marker(self, player):
        marker = self._get_marker(player)
        color = self._get_color(marker)
        return Colorist.color_text(marker, color)


    def _get_marker(self, player_id):
        return Validator.handle_input(get_marker, "marker_input", [player_id])

    def _get_color(self, what_gets_colored):
        return Validator.handle_input(get_color, "color_name", [what_gets_colored])

    def _markers_need_filling(self):
       return (self.first_marker is None) or (self.second_marker is None)

    def _markers_match(self):
        (self.first_marker == self.second_marker and self.color1 == self.color2)

    @classmethod
    def setup_view(cls, players=["Player 1", "Player 2"]):
        view_setup = cls()
        view_setup._set_up_players(players)
        return view_setup


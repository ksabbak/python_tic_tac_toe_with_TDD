from .validator import Validator
from .command_line_views.colorist import Colorist
from .command_line_views.board_decorator import BoardDecorator
from .command_line_views.view_getter import ViewGetter

class ViewSetup:
    def __init__(self):
        self.board_color = None
        self.player_markers = []

    @classmethod
    def setup_view(cls, players=["Player 1", "Player 2"]):
        view_setup = cls()
        view_setup._set_up_players(players)
        view_setup.board_color = view_setup._get_color("the board")
        return BoardDecorator(view_setup)

    def _set_up_players(self, players):
        for player in players:
            self._add_player(player)

    def _add_player(self, player):
        successful = False
        while not successful:
            colored_marker = self._get_colored_marker(player)
            potential_markers = self.player_markers + [colored_marker]
            if Validator().no_matches(potential_markers):
                self.player_markers.append(colored_marker)
                successful = True

    def _get_colored_marker(self, player):
        marker = self._get_marker(player)
        color = self._get_color(marker)
        return Colorist.color_text(marker, color)


    def _get_marker(self, player_id):
        return Validator().handle_input(ViewGetter.get_marker, "marker_input", [player_id])

    def _get_color(self, what_gets_colored):
        return Validator().handle_input(ViewGetter.get_color, "color_name", [what_gets_colored])



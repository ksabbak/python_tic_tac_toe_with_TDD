from .colorist import Colorist

class BoardDecorator:
    def __init__(self, view_setup):
        self.player_markers = view_setup.player_markers
        self.board_color = view_setup.board_color

    def get_marker_for_current_turn(self, turn, players):
        return self.player_markers[turn % len(players)]



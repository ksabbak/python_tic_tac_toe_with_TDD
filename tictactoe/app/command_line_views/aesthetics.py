from .colorist import Colorist

class Aesthetics:
    def __init__(player_markers, player_colors=["", ""], board_color=""):
        self.player_markers = _merge_markers(player_markers, player_colors)
        self.board_color = board_color

    def _merge_markers(self, markers, colors):
        return (map(lambda marker, color: Colorist.color_text(color, text), markers, colors))


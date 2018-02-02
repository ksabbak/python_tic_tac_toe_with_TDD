from .colorist import Colorist

class BoardDecorator:
    def __init__(self, player_markers, player_colors=["", ""], board_color=""):
        self.player_markers = self._merge_markers(player_markers, player_colors)
        self.board_color = board_color

    def _merge_markers(self, markers, colors):
        return list(map(lambda marker, color: Colorist.color_text(marker, color), markers, colors))


from .colorist import Colorist

class BuildABoard:
    def __init__(board, aesthetics, last_move):
        self.board = board
        self.board_color = aesthetics.board_color
        self.markers = aesthetics.markers
        self.last_move = last_move

    def printable_board():
        return self._build_board(self._mark_spaces())


    def _build_board(marked_spaces):
            board_str = Colorist.color_text(_build_horizontal_coordinates(), self.board_color)
            for space in range(0, len(self.board.spaces)):
                if space % self.board.side_length == 0:
                    board_str += self._add_vertical_coordinate(space)
                board_str += self._fill_standard_square
                if self._is_space_at_end_of_row(space) and not self._is_space_at_end_of_board(space):
                    board_str = self._replace_extraneous_end_chars_with_new_line(board_str)
                    board_str += Colorist.color_text(_build_filler_row(), self.board_color)
            return self._replace_extraneous_end_chars_with_new_line(board_str)

    def _build_horizontal_coordinates(self):
        first_row = ""
        for num in range(1, self.board.side_length + 1):
            first_row += "   " + str(num)
        first_row += "\n"
        return first_row

    def _build_filler_row(self):
        filler_row = "  ==="
        for row in range(1, self.board.side_length):
            filler_row += "+==="
        filler_row += "\n"
        return filler_row

    def _add_vertical_coordinate(self, space):
        return Colorist.color_text(board.coordinates[space][0], self.board_color) + " "

    def _fill_standard_square(self, space):
        return " " + color_spaces[space] + Colorist.color_text(" |", self.board_color)

    def _replace_extraneous_end_chars_with_new_line(self, board_str):
        return board_str[:-5] + "\033[0m" + "\n"

    def _is_space_at_end_of_row(space):
        space % self.board.side_length == self.board.side_length - 1

    def _is_space_at_end_of_board(space):
        return space == len(self.board.spaces) - 1

    def _mark_spaces(self):
        new_spaces = []
        for i, space in enumerate(self.board.spaces):
            if space is not " ":
                player = i % len(self.markers)
                new_space = self.markers[player]
            else:
                new_space = space

            if i == self.last_move:
                new_space = Colorist.color_text(new_space, "\033[;4m")
            new_spaces.append(new_space)
        return new_spaces

    def _mark_spaces(self):

from ..end_conditions import all_win_conditions

class Board:
    def __init__(self, board, color):
        self.spaces = board
        self.side_length = int(len(self.spaces) ** (1 / 2))
        self.all_win_conditions = self._set_win_conditions()
        self.coordinates = self._build_coordinates()
        self.color = color

    @classmethod
    def create_fresh_board(cls, length=9, color=""):
        board = ()
        for i in range(0, length):
            board += (" ",)
        return cls(board, color)

    @classmethod
    def create_from_existing_spaces(cls, spaces, color=""):
        board = tuple(spaces)
        return cls(board, color)


    def mark_space(self, space, marker):
        if self.space_is_empty(space):
            self._change_space(space, marker)

    def clear_space(self, space):
        if not self.space_is_empty(space):
            self._change_space(space, " ")

    def is_full(self):
        return not self.empty_spaces()

    def space_is_empty(self, space):
        return self.spaces[space] == " "

    def empty_spaces(self):
        return [space for space in range(0, len(self.spaces))
                if self.space_is_empty(space)]

    def winning_marker(self):
        for win_condition in self.all_win_conditions:
            board_sample = list(map(lambda x: self.spaces[x], win_condition))
            if (len(set(board_sample)) == 1
               and not self.space_is_empty(win_condition[0])):
                return board_sample[0]

    def space_string(self):
        space_string = ""
        for space in self.spaces:
            space_string += str(space)
        return space_string


    def _change_space(self, space, marker):
        spaces = list(self.spaces)
        spaces[space] = marker
        self.spaces = tuple(spaces)

    def _build_coordinates(self):
        coords = []
        for alpha in range(ord("A"), ord("A") + self.side_length):
            for num in range(1, self.side_length + 1):
                coords.append(chr(alpha) + str(num))
        return coords

    def _set_win_conditions(self):
        self.all_win_conditions = None
        return all_win_conditions(self)

from textwrap import dedent

class Board:
    def __init__(self, board, color):
        self.spaces = board
        self.side_length = int(len(self.spaces) ** (1 / 2))
        self.all_win_conditions = None
        self.coordinates = self._build_coordinates()
        self.color = color

    @classmethod
    def create_from_scratch(cls, length=9, color=""):
        board = ()
        for i in range(0, length):
            board += (" ",)
        return cls(board, color)

    @classmethod
    def create_from_existing(cls, spaces, color=""):
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
        for win_condition in self._all_win_conditions():
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


# END CONDITIONS: 
    def _all_win_conditions(self):
        self.all_win_conditions = self.all_win_conditions or self._horizontal_win_conditions() + self._vertical_win_conditions() + self._diagonal_win_conditions()
        return self.all_win_conditions

    def _horizontal_win_conditions(self):
        wins = []
        for i in range(0, self.side_length):
            wins.append(self._calculate_win_conditions(1, self.side_length * i))
        return wins

    def _vertical_win_conditions(self):
        wins = []
        for i in range(0, self.side_length):
            wins.append(self._calculate_win_conditions(self.side_length, i))
        return wins

    def _diagonal_win_conditions(self):
        wins = []
        wins.append(self._calculate_win_conditions(self.side_length + 1, 0))
        wins.append(self._calculate_win_conditions(self.side_length - 1, self.side_length - 1))
        return wins

    def _calculate_win_conditions(self, incrementor, addition):
        lst = []
        for space in range(0, self.side_length):
            lst.append(space * incrementor + addition)
        return lst

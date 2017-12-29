from textwrap import dedent

class Board:
    def __init__(self, length=9, color=""):
        self._build_board(length)
        self.side_length = int(len(self.spaces) ** (1 / 2))
        self.all_win_conditions = None
        self.coordinates = self._build_coordinates()
        self.color = color

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

    def __str__(self):
        return self._build_board_str()

    def winning_marker(self):
        for win_condition in self._all_win_conditions():
            board_sample = list(map(lambda x: self.spaces[x], win_condition))
            if (len(set(board_sample)) == 1 
               and not self.space_is_empty(win_condition[0])):
                return board_sample[0]


    def _change_space(self, space, marker):
        spaces = list(self.spaces)
        spaces[space] = marker
        self.spaces = tuple(spaces)

# BUILDING: 
    def _build_board(self, length):
        i = 0
        self.spaces = ()
        while i < length:
            self.spaces += (" ",)
            i += 1

    def _build_coordinates(self):
        coords = []
        for alpha in range(ord("A"), ord("A") + self.side_length):
            for num in range(1, self.side_length + 1):
                coords.append(chr(alpha) + str(num))
        return coords

    def _build_board_str(self):
        first_row = self._color_text(self._build_first_row())
        filler_row = self._color_text(self._build_filler_row())
        board = first_row
        for space in range(0, len(self.spaces)):
            if space % self.side_length == 0:
                board += self._color_text(self.coordinates[space][0]) + " "
            board += self._color_text(" %s |" % self.spaces[space])
            if (space % self.side_length == self.side_length - 1
                 and space != len(self.spaces) -1 ):
                board = board[:-1]
                board += "\n" + filler_row
        return board[:-1] + "\n"

    # BUILD BOARD - HELPER METHODS:

    def _build_first_row(self):
        first_row = ""
        for num in range(1, self.side_length + 1):
            first_row += "   " + str(num)
        first_row += "\n" 
        return first_row

    def _build_filler_row(self):
        filler_row = "  ==="
        for row in range(1, self.side_length):
            filler_row += "+==="
        filler_row += "\n" 
        return filler_row
        
    def _color_text(self, str):
        no_color = '\033[0m'
        return str


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

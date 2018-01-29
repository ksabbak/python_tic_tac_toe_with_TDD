class Board:
    def __init__(self, board):
        self.spaces = board
        self.side_length = int(len(self.spaces) ** (1 / 2))
        self.coordinates = self._build_coordinates()

    @classmethod
    def create_fresh_board(cls, length=9):
        board = ()
        for i in range(0, length):
            board += (" ",)
        return cls(board)

    @classmethod
    def create_from_existing_spaces(cls, spaces):
        board = tuple(spaces)
        return cls(board)


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



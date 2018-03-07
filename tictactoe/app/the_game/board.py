class Board:
    def __init__(self, board):
        self.spaces = board

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

    def side_length(self):
        return int(len(self.spaces) ** (1 / 2))

    def mark_space(self, space, turn):
        if self.space_is_empty(space):
            self._change_space(space, turn)

    def clear_space(self, space):
        if not self.space_is_empty(space):
            self._change_space(space, " ")

    def is_full(self):
        return not self.empty_spaces()

    def space_is_empty(self, space):
        return self.spaces[space] == " "

    def empty_spaces(self):
        return [space for space in range(len(self.spaces))
                if self.space_is_empty(space)]

    def space_string(self):
        return "".join(str(space) for space in self.spaces)


    def _change_space(self, space, turn):
        spaces = list(self.spaces)
        spaces[space] = turn
        self.spaces = tuple(spaces)


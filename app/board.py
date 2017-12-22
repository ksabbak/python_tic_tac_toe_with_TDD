from textwrap import dedent

class Board:
    def __init__(self, length=9):
        self.spaces = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.side_length = int(len(self.spaces) ** (1/2))

    def mark_space(self, space, marker):
        if self.space_is_empty(space):
            spaces = list(self.spaces)
            spaces[space] = marker
            self.spaces = tuple(spaces)

    def is_full(self):
        return not self.empty_spaces()

    def space_is_empty(self, space):
        return self.spaces[space] == space

    def empty_spaces(self): 
        return [space for space in range(0, len(self.spaces)) 
                if self.space_is_empty(space)]

    def to_str(self):
        pretty_board = """\
           1   2   3 
        A  %s | %s | %s
          ===+===+===
        B  %s | %s | %s
          ===+===+===
        C  %s | %s | %s  
            """ % self.spaces       
        return dedent(pretty_board)

    def _build_board(self, length)
        i = 0
        self.spaces = ()
        while i < length:
            self.spaces.append(" ")
            i += 1

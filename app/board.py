class Board:
    def __init__(self):
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
         return(" %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % self.spaces)


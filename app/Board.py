class Board:
    def __init__(self):
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def mark_space(self, space, marker):
        if isinstance(self.spaces[space], int):
            self.spaces[space] = marker

    def is_full(self):
        for space in self.spaces:
            if isinstance(space, int): return False 
        return True


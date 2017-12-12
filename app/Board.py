class Board:
    def __init__(self):
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def mark_space(self, space, marker):
        self.spaces[space] = marker

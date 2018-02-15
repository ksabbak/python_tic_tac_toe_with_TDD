class Coordinate:
    def __init__(self, side_length):
        self.coordinates = self._build_coordinates(side_length)

    def number_to_coordinate(self, move):
        if move is not None: return self.coordinates[move]

    def coordinate_to_number(self, move):
        move = self._format_move_input(move)
        if move in self.coordinates:
            return self.coordinates.index(move)

    def _format_move_input(self, move):
        coord_list = list(move.upper())
        coord_list.sort()
        coord_list.reverse()
        return "".join(coord_list)

    def _build_coordinates(self, side_length):
        coords = []
        for letter in range(ord("A"), ord("A") + side_length):
            for number in range(1, side_length + 1):
                coords.append(chr(letter) + str(number))
        return coords

class GameMoves:
    def __init__(self):
        self.moves = ()

    def append(self, move):
        self.moves += (move, )
        return self.moves

    def undo(self, players):
        for i in range(0, len(players)):
            self._delete_last_move()
        return self.moves

    def __len__(self):
        return len(self.moves)

    def _delete_last_move(self):
        move_list = list(self.moves)
        move_list.pop()
        self.moves = tuple(move_list)

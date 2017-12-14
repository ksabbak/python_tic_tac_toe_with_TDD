class Player:
    def __init__(self, marker):
        self.marker = marker

    def get_move(self):
        #This is not single responsibility.
        print("Where would you like to move?")
        move = input()
        return int(move)

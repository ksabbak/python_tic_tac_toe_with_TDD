from .game import Game
from .player import HumanPlayer
from .ai import AI
from .view import print_intro_text, print_instructions

class Controller:
    def run(self):
        print_intro_text()
        print_instructions()
        game_choice = input().strip()
        game = None
        if game_choice in "1":
            game = Game(HumanPlayer("x"), HumanPlayer("o"))
        elif game_choice in "2":
            game = Game.mixed_game({"player1" : HumanPlayer("x"),  "player2" : AI("o")})
        else:
            game = Game(AI("x"), AI("o"))
        game.play()



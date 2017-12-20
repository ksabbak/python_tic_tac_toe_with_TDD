from .game import Game
from .player import Player
from .ai import AI
from .view import print_intro_text, print_instructions

class Controller:
    def run(self):
        print_intro_text()
        print_instructions()
        game_choice = input().strip()
        game = None
        if game_choice in "1":
            game = Game(Player("x"), Player("o"))
        elif game_choice in "2":
            game = Game.mixed_game({"player1" : Player("x"),  "player2" : AI("o")})
        else:
            game = Game(AI("x"), AI("o"))
        game.play()



from .game import Game
from .player import HumanPlayer
from .ai import AI
from .view import print_intro_text, print_instructions, get_game_type_input, print_sorry

class Controller:
    def run(self):
        print_intro_text()
        print_instructions()
        game_choice = self._handle_input(get_game_type_input, ["1", "2", "3"])
        game = None
        if game_choice in "1":
            game = Game(HumanPlayer("x"), HumanPlayer("o"))
        elif game_choice in "2":
            game = Game.mixed_game({"player1" : HumanPlayer("x"),  "player2" : AI("o")})
        else:
            game = Game(AI("x"), AI("o"))
        game.play()

    
    def _play(self, game):
        print_new_turn(game.board)
        while not game.is_over():
            game.take_a_turn()
        print_game_over(winner(self.board))



    def _handle_input(self, input_getter, acceptable_input):
        user_input = None
        while user_input is None: 
            user_input = input_getter()
            if user_input not in acceptable_input or user_input is None: 
                user_input = None
                print_sorry()
            else:
                return user_input

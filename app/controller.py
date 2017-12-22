from .game import Game
from .player import HumanPlayer
from .ai import AI
from .view import print_intro_text, print_instructions, get_game_type_input, print_sorry, print_new_turn, print_game_over, get_player_move

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
        self._play(game)

    
    def _play(self, game):
        print_new_turn(game.board)
        while not game.is_over():
            if not game.current_player.is_ai():
                move = get_player_move()
                game.take_a_turn(move)
            else:
                move = game.take_a_turn()
            game.current_player.print_update(game.board, move)
        print_game_over(game.winner())

    def _handle_input(self, input_getter, acceptable_input, arguments=[]):
        user_input = None
        while user_input is None: 
            user_input = input_getter(*arguments)
            if user_input not in acceptable_input: 
                user_input = None
                print_sorry()
            else:
                return user_input

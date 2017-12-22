from .game import Game
from .player import HumanPlayer
from .ai import AI
from .view import print_intro_text, print_instructions, get_game_type_input, print_sorry, print_new_turn, print_game_over, get_player_move, print_ai_update, print_humanplayer_update, get_marker, get_who_first

class Controller:
    def run(self):
        print_intro_text()
        print_instructions()
        game_choice = self._handle_input(get_game_type_input, ["1", "2", "3"])
        game = None
        if game_choice in "1":
            player1, player2 = self._get_markers("Player 1", "Player 2")
            game = Game(HumanPlayer(player1), HumanPlayer(player2))
        elif game_choice in "2":
            who_first = get_who_first()
            human_player, ai = self._get_markers("you", "the computer")
            if self._affirmative(who_first):
                game = Game.mixed_game({"player1" : HumanPlayer(human_player),  "player2" : AI(ai)})
            else:
                game = Game.mixed_game({"player2" : HumanPlayer(human_player),  "player1" : AI(ai)})
        elif game_choice in "3":
            player1, player2 = self._get_markers("Computer 1", "Computer 2")
            game = Game(AI(player1), AI(player2))
        else:
            print("This program will self-destruct")
            return
        self._play(game)


    def _play(self, game):
        print_new_turn(game.board)
        while not game.is_over():
            if not game.current_player.is_ai():
                self._human_player_turn(game)
            else:
                self._ai_player_turn(game)
            game.end_turn()
        print_game_over(game.winner())

    def _human_player_turn(self, game):
        acceptable_input = list(map(str, game.board.empty_spaces()))
        move = self._handle_input(get_player_move, acceptable_input, game.current_player.marker)
        game.start_turn(move)
        print_humanplayer_update(game.board, game.current_player.marker, move)

    def _ai_player_turn(self, game):
        move = game.start_turn()
        print_ai_update(game.board, game.current_player.marker, move)

    def _get_markers(self, player1, player2):
        first_marker = None
        second_marker = None
        while first_marker == second_marker:
            first_marker = get_marker(player1)[0]
            second_marker = get_marker(player2)[0]
            if first_marker == second_marker:
                print_sorry()
        return[first_marker, second_marker] 

    def _affirmative(self, response):
        response = response.lower()
        return (response != "n") and (response in "yes yeah definitely affirmative okay yup sure true")

    def _handle_input(self, input_getter, acceptable_input, arguments=[]):
        user_input = None
        while user_input is None: 
            user_input = input_getter(*arguments)
            if user_input not in acceptable_input: 
                user_input = None
                print_sorry()
            else:
                return user_input

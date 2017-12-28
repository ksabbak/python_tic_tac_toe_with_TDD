from string import punctuation

from .game import Game
from .player import HumanPlayer
from .ai import AI
from .view import print_intro_text, print_instructions, get_game_type_input, print_sorry, print_new_turn, print_game_over, get_player_move, print_ai_update, print_humanplayer_update, get_marker, get_who_first, print_who_first

class Controller:
    def __init__(self):
        self.game = Game(AI("x"), AI("o"))
        
    def run(self):
        print_intro_text()
        print_instructions()
        game_choice = self._handle_input(get_game_type_input, self._acceptable_game_type_input)
        if game_choice in "1":
            player1, player2 = self._get_markers("Player 1", "Player 2")
            self.game = Game(HumanPlayer(player1), HumanPlayer(player2))
        elif game_choice in "2":
            player_first = self._affirmative(get_who_first())
            print_who_first(player_first)
            human_player, ai = self._get_markers("you", "the computer")
            if player_first:
                self.game = Game.mixed_game({"player1" : HumanPlayer(human_player),  "player2" : AI(ai)})
            else:
                self.game = Game.mixed_game({"player2" : HumanPlayer(human_player),  "player1" : AI(ai)})
        elif game_choice in "3":
            player1, player2 = self._get_markers("Computer 1", "Computer 2")
            self.game = Game(AI(player1), AI(player2))
        else:
            print("This program will self-destruct")
            return
        self._play()


    def _play(self):
        print_new_turn(self.game.board)
        while not self.game.is_over():
            if self.game.current_player.is_ai():
                self._ai_player_turn()
            else:
                self._human_player_turn()
            self.game.end_turn()
        print_game_over(self.game.winner())

    def _human_player_turn(self):
        move = self._handle_input(get_player_move, self._acceptable_move_input, [self.game.current_player.marker])
        if move == "undo":
            self.game.undo_turn()
            move = self.game.current_player.moves[-1] if self.game.current_player.moves else None
        else:
            move = self._coordinate_to_number(move)
            self.game.start_turn(move) 
        print_humanplayer_update(self.game.board, self.game.current_player.marker, self._number_to_coordinate(move))

    def _ai_player_turn(self):
        move = self.game.start_turn()
        print_ai_update(self.game.board, self.game.current_player.marker, self._number_to_coordinate(move))

    def _get_markers(self, player1, player2):
        first_marker = None
        second_marker = None
        while first_marker == second_marker:
            first_marker = self._handle_input(get_marker, self._acceptable_marker_input, [player1])
            second_marker = self._handle_input(get_marker, self._acceptable_marker_input, [player2])
            if first_marker == second_marker or (first_marker is None) or (second_marker is None):
                print_sorry("match marker")

        return[first_marker, second_marker]

    def _affirmative(self, response):
        response = response.lower().strip(punctuation)
        return (response != "n") and (response in "yes yeah definitely affirmative okay yup sure true")

    def _coordinates(self):
        return self.game.board.coordinates

    def _coordinate_to_number(self, move):
        move = self._format_move_input(move)
        if move in self._coordinates():
            return self._coordinates().index(move)

    def _number_to_coordinate(self, move):
        if move is not None: return self._coordinates()[move]

    def _format_move_input(self, move):
        coord_list = list(move.upper())
        coord_list.sort()
        coord_list.reverse()
        return "".join(coord_list)

    def _acceptable_marker_input(self, marker_input):
        if len(marker_input) != 1:
            return "marker length"

    def _acceptable_game_type_input(self, game_type_input):
        if game_type_input not in ["1", "2", "3"]:
            return "game type"

    def _acceptable_move_input(self, move_input):
        if move_input == "undo": return
        move_input = self._format_move_input(move_input)
        move_input = self._coordinate_to_number(move_input)
        if move_input is None:
            return "no coord"
        if move_input not in self.game.board.empty_spaces():
            return "taken"

    def _handle_input(self, input_getter, input_parser, arguments=[]):
        user_input = None
        while user_input is None: 
            user_input = input_getter(*arguments)
            unacceptable_input = input_parser(user_input)
            if unacceptable_input:
                user_input = None
                print_sorry(unacceptable_input)
            else:
                return user_input

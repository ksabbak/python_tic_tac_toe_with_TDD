from string import punctuation

from .__init__ import Game
from .validator import Validator
from .move_coordinates_validator import MoveCoordinatesValidator
from .command_line_views.view_getters import get_player_move
from .command_line_views.view_printer import print_intro_text, print_instructions, print_new_turn, print_game_over, print_ai_update, print_humanplayer_update, print_board_size, print_ai_thinking
from .command_line_views.coordinate import Coordinate
from .game_settings_getter import GameSettingsGetter
from .view_setup import ViewSetup


class Controller:
    def __init__(self):
        self.game = Game.cvc(9)

    def run(self):
        self._setup()
        self._play()
        print_game_over(self.board_decorator, self.game.players, self.game.winner())

    def _setup(self):
        print_intro_text()
        print_board_size()
        board_choice = GameSettingsGetter().make_board_choice()
        print_instructions()
        self.game = GameSettingsGetter().impliment_game_choice(board_choice)
        self.board_decorator = ViewSetup().setup_view()
        self.coordinates = Coordinate(self.game.board.side_length())


    def _play(self):
        print_new_turn(self.game.board, self.board_decorator, self.game.last_move)
        while not self.game.is_over():
            if self.game.current_player.is_ai():
                self._ai_player_turn()
            else:
                self._human_player_turn()
            self.game.end_turn()

    def _human_player_turn(self):
        move = MoveCoordinatesValidator(self.game.board).handle_input(get_player_move, "move_input", [self.board_decorator.player_markers[self.game.turn % 2]])
        if move == "undo":
            self.game.undo_turn()
        else:
            self.game.start_turn(self.coordinates.coordinate_to_number(move))
        move = self.game.last_move
        print_humanplayer_update(self.game.board, self.board_decorator, self.coordinates.number_to_coordinate(move), self.game.turn)

    def _ai_player_turn(self):
        print_ai_thinking()
        move = self.game.start_turn()
        print_ai_update(self.game.board, self.board_decorator, self.coordinates.number_to_coordinate(move), self.game.turn)

    def _number_to_coordinate(self, move):
        if move is not None: return self.game.board.coordinates[move]

    def _coordinate_to_number(self, move):
        move = self._format_move_input(move)
        if move in self.board.coordinates:
            return self.board.coordinates.index(move)


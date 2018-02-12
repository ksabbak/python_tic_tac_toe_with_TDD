from string import punctuation

from .__init__ import Game
from .validator import Validator
from .command_line_views.view_getters import get_game_type_input, get_player_move,  get_marker, get_who_first, get_color
from .command_line_views.view_printer import print_intro_text, print_instructions, print_new_turn, print_game_over, print_ai_update, print_humanplayer_update, print_who_first, print_board_size, print_ai_thinking
from .command_line_views.colorist import Colorist
from .command_line_views.board_decorator import BoardDecorator
from .game_settings_getter import GameSettingsGetter
from .view_setup import ViewSetup


class Controller:
    def __init__(self):
        self.game = Game.cvc(9)

    def run(self):
        print_intro_text()
        print_board_size()
        board_choice = GameSettingsGetter().make_board_choice()
        print_instructions()
        GameSettingsGetter().impliment_game_choice(board_choice)
        self._get_markers_and_colors()
        self._play()

    def _create_game(self, new_game, board_choice, players):
        self._get_markers_and_colors(*players)
        self.game = new_game(board_choice)

    def _play(self):
        print_new_turn(self.game.board, self.board_decorator, self.game.last_move)
        while not self.game.is_over():
            if self.game.current_player.is_ai():
                self._ai_player_turn()
            else:
                self._human_player_turn()
            self.game.end_turn()
        print_game_over(self.board_decorator, self.game.players, self.game.winner())

    def _human_player_turn(self):
        move = Validator().handle_input(get_player_move, self._acceptable_move_input, [self.board_decorator.player_markers[self.game.turn % 2]])
        if move == "undo":
            self.game.undo_turn()
        else:
            self.game.start_turn(self._coordinate_to_number(move))
        move = self.game.last_move
        print_humanplayer_update(self.game.board, self.board_decorator, self._number_to_coordinate(move), self.game.turn)

    def _ai_player_turn(self):
        print_ai_thinking()
        move = self.game.start_turn()
        print_ai_update(self.game.board, self.board_decorator, self._number_to_coordinate(move), self.game.turn)

    def _get_markers_and_colors(self):
        board_decorator = ViewSetup().setup_view()
        self.board_decorator = board_decorator
        return board_decorator

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

    # def _acceptable_marker_input(self, marker_input):
    #     if len(marker_input) != 1 or marker_input == " ":
    #         return "marker length"

    # def _acceptable_game_type_input(self, game_type_input):
    #     if game_type_input not in ["1", "2", "3"]:
    #         return "game type"

    # def _acceptable_board_type_input(self, board_type_input):
    #     if board_type_input not in ["1", "2"]:
    #         return "board type"

    # def _acceptable_color_input(self, color_input):
    #     color_input = color_input.lower().strip(punctuation)
    #     if color_input == "none": return None
    #     for color in Colorist.color_names():
    #         if color_input == color.lower(): return None
    #     return "color"

    # def _acceptable_move_input(self, move_input):
    #     if move_input == "undo": return
    #     move_input = self._format_move_input(move_input)
    #     move_input = self._coordinate_to_number(move_input)
    #     if move_input is None:
    #         return "no coord"
    #     if move_input not in self.game.board.empty_spaces():
    #         return "taken"

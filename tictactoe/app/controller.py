from .__init__ import Game
from .command_line_views.view_printer import ViewPrinter
from .command_line_views.coordinate import Coordinate
from .game_settings_getter import GameSettingsGetter
from .view_setup import ViewSetup
from .command_line_player import CommandLinePlayer

class Controller:
    def run(self):
        command_line_player = self._setup()
        command_line_player.play()
        ViewPrinter.print_game_over(command_line_player.board_decorator, command_line_player.game.players, command_line_player.game.winner())

    def _setup(self):
        ViewPrinter.print_intro_text()
        board_choice = self._setup_board()
        ViewPrinter.print_instructions()
        game = GameSettingsGetter().impliment_game_choice(board_choice)
        board_decorator = ViewSetup().setup_view()
        coordinates = Coordinate(game.board.side_length())
        return CommandLinePlayer(**{"game": game, "board_decorator": board_decorator, "coordinates": coordinates})


    def _setup_board(self):
        ViewPrinter.print_board_size()
        return GameSettingsGetter().make_board_choice()

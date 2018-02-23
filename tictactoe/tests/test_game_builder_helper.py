import pytest
from tictactoe.web_app.game_builder_helper import GameBuilderHelper
from tictactoe.app.the_game.game import Game

@pytest.fixture()
def game_builder_helper():
    return GameBuilderHelper()

def test_error_handling_for_set_up_no_game_type(game_builder_helper):
    form = {  "board": "9" }
    error = game_builder_helper.error_handling_for_setup(form)
    assert error == "You must pick a board size and game type"

def test_error_handling_for_set_up_no_board(game_builder_helper):
    form = {  "game_type": "pvp" }
    error = game_builder_helper.error_handling_for_setup(form)
    assert error == "You must pick a board size and game type"

def test_error_handling_for_set_up_missing_player1_marker(game_builder_helper):
    form = {  "game_type": "pvc", "board": "9", "player1": "", "player2": "b" }
    error = game_builder_helper.error_handling_for_setup(form)
    assert error == "Please enter your marker choices"

def test_error_handling_for_set_up_missing_player2_marker(game_builder_helper):
    form = {  "game_type": "pvc", "board": "9", "player1": "a", "player2": "" }
    error = game_builder_helper.error_handling_for_setup(form)
    assert error == "Please enter your marker choices"

def test_error_handling_for_set_up_matching_markers(game_builder_helper):
    form = {  "game_type": "pvc", "board": "9", "player1": "a", "player2": "a" }
    error = game_builder_helper.error_handling_for_setup(form)
    assert error == "The markers shouldn't match"

def test_build_game_with_board(game_builder_helper):
    session = {"type": "pvp"}
    board = 9
    game = game_builder_helper.build_game(board, session)
    assert hasattr(game, "players")
    assert len(game.board.spaces) == 9
    assert len(game.board.empty_spaces()) ==9

def test_build_game_with_session_board(game_builder_helper):
    session = {"type": "pvp", "board": "010      "}
    game = game_builder_helper.build_game(session=session)
    assert game.board.space_string() == "010      "

def test_build_game_with_nothing(game_builder_helper):
    session = { "board": None }
    game = game_builder_helper.build_game(session=session)
    assert game == "error!"


def test_board_view_builder_9_empty_spaces(game_builder_helper):
    spaces = "         "
    session = {'players': "xo"}
    view_board = game_builder_helper.board_view_builder(spaces, session)
    assert view_board == spaces

def test_board_view_builder_empty_string(game_builder_helper):
    spaces = ""
    session = {'players': "xo"}
    view_board = game_builder_helper.board_view_builder(spaces, session)
    assert view_board == spaces

def test_board_view_builder_board_has_moves(game_builder_helper):
    spaces = "010      "
    session = {'players': "xo"}
    view_board = game_builder_helper.board_view_builder(spaces, session)
    assert view_board == "xox      "


def test_undo_board_view_9_empty_spaces(game_builder_helper):
    board_view = "         "
    session = {'players': "xo"}
    spaces = game_builder_helper.undo_board_view(board_view, session)
    assert spaces == board_view

def test_undo_board_view_empty_string(game_builder_helper):
    board_view = ""
    session = {'players': "xo"}
    spaces = game_builder_helper.undo_board_view(board_view, session)
    assert spaces == board_view

def test_undo_board_view(game_builder_helper):
    board_view = "xox      "
    session = {'players': "xo"}
    spaces = game_builder_helper.undo_board_view(board_view, session)
    assert spaces == "010      "

def test_set_game_sessions(game_builder_helper):
    form = {
            "player1": "x",
            "player2": "o",
            "bgcolor": "#000000",
            "color1": "#0000ff",
            "color2": "#ff0000"
            }
    session = {}
    game = Game.pvp(9)
    game_builder_helper.set_game_sessions(game, form, session)
    assert session["players"] == "xo"
    assert session["colors"] == ["#0000ff", "#ff0000"]
    assert session["bgcolor"] == "#000000"
    assert session["board"] == game.board.space_string()

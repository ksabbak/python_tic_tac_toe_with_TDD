import pytest
from tictactoe.web_app.turn_helper import TurnHelper
from tictactoe.app.the_game.game import Game

@pytest.fixture
def turn_helper():
    return TurnHelper()


def test_get_next_render_data_game_over(turn_helper):
    game = Game.pvp(9)
    session={"result": "You won!"}
    data = turn_helper.get_next_render_data(game, session)
    assert data == {"redirect": '/game-over'}

def test_get_next_render_data_ai_turn(turn_helper):
    game = Game.cvc(9)
    session={}
    data = turn_helper.get_next_render_data(game, session)
    assert data == {
                    "template_name_or_list": 'ai_board.html',
                    "board": game.board.space_string(),
                    "length": game.board.side_length()
                    }
    assert session["ai"] is True
    assert session['turn'] == game.current_player.turn_order

def test_get_next_render_data_human_turn(turn_helper):
    game = Game.pvp(9)
    session={}
    data = turn_helper.get_next_render_data(game, session)
    assert data == {
                    "template_name_or_list": 'board.html',
                    "board": game.board.space_string(),
                    "length": game.board.side_length()
                    }
    assert session["ai"] is False
    assert session['turn'] == game.current_player.turn_order

def test_check_game_over_player_winner(turn_helper):
    session = {}
    game = Game.pvp(9, list("111      "))
    turn_helper.check_game_over(game, session)
    assert session["length"] == 3
    assert session["result"] == "You won! 😃"

def test_check_game_over_player_loser(turn_helper):
    session = {}
    game = Game.cvp(9, list("000      "))
    turn_helper.check_game_over(game, session)
    assert session["length"] == 3
    assert session["result"] == "You lost 😱"

def test_check_game_over_no_winner(turn_helper):
    session = {}
    game = Game.cvp(9, list("101010010"))
    turn_helper.check_game_over(game, session)
    assert session["length"] == 3
    assert session["result"] == "Game over, no one wins. 🙃"

def test_start_turn_with_move(turn_helper):
    session = {"board": "010      ", "type": "pvp"}
    game = turn_helper.start_turn(4, session)
    assert game.board.space_string() == session["board"]
    assert game.board.space_string() == "010 3    "

def test_start_turn_without_move(turn_helper):
    session = {"board": "010      ", "type": "cvc"}
    game = turn_helper.start_turn(session=session)
    assert game.board.space_string() == session["board"]
    assert len(game.board.empty_spaces()) == 5


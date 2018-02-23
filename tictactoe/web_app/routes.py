import time

from flask import render_template, redirect, request, session, url_for
from tictactoe.web_app import web_app
from .game_builder_helper import GameBuilderHelper
from .turn_helper import TurnHelper

@web_app.before_request
def before_request():
    if 'type' not in session and request.endpoint in ['update_board', 'ai_board', 'game_over']:
        return redirect(url_for('board_new'))


@web_app.route('/index')
@web_app.route('/')
def index():
    return redirect("/board/new")
@web_app.route('/board/new')
def board_new():
    session.clear()
    return render_template('index.html')

@web_app.route('/board/create', methods=["POST"])
def create_board():
    game_builder_helper = GameBuilderHelper()
    error = game_builder_helper.error_handling_for_setup(request.form)
    if error:
        return render_template('index.html', errors=error)
    session["type"] = request.form["game_type"]
    game = game_builder_helper.build_game(board=request.form["board"])
    game_builder_helper.set_game_sessions(game, request.form)
    next_step = TurnHelper().get_next_render_data(game)
    if "redirect" in next_step.keys():
        return redirect(next_step["redirect"])
    else:
        return render_template(**next_step)

@web_app.route('/board', methods=['POST'])
def update_board():
    if request.form["submit"] == "submit":
        game = TurnHelper().take_normal_turn(request.form)
    else:
        game = TurnHelper().undo_turn()
    TurnHelper().check_game_over(game)
    game.end_turn()
    next_step = TurnHelper().get_next_render_data(game)
    if "redirect" in next_step.keys():
        return redirect(next_step["redirect"])
    else:
        return render_template(**next_step)


@web_app.route('/board')
def ai_board():
    print("Board = " + session["board"])
    game = TurnHelper().start_turn()
    game.end_turn()
    TurnHelper().check_game_over(game)
    next_step = TurnHelper().get_next_render_data(game)
    if "redirect" in next_step.keys():
        return redirect(next_step["redirect"])
    else:
        return render_template(**next_step)

@web_app.route('/game-over')
def game_over():
    board = GameBuilderHelper().board_view_builder(session["board"])
    return render_template('end.html', board=board, length=session["length"], result=session["result"])



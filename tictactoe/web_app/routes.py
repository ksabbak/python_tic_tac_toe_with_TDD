import time

from flask import render_template, redirect, request, session, url_for
from tictactoe.web_app import web_app
from .route_helpers import end_conditions, render_next, build_game, start_turn, undo_board_view, board_view_builder, take_normal_turn, undo_turn

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
    return render_template('index.html')

@web_app.route('/board/create', methods=["POST"])
def create_board():
    if "game_type" not in request.form or "board" not in request.form:
        session.clear()
        return render_template('index.html', errors="You must pick a board size and game type")
    session["type"] = request.form["game_type"]
    game = build_game(board=request.form["board"])
    session["players"] = "xo"
    session["board"] = game.board.space_string()
    return render_next(game)


@web_app.route('/board', methods=['POST'])
def update_board():
    if request.form["submit"] == "submit":
        game = take_normal_turn()
    else:
        game = undo_turn()
    end_conditions(game)
    game.end_turn()
    return render_next(game)


@web_app.route('/board')
def ai_board():
    print("Board = " + session["board"])
    game = start_turn()
    game.end_turn()
    end_conditions(game)
    return render_next(game)

@web_app.route('/game-over')
def game_over():
    result = session["result"]
    board = board_view_builder(session["board"])
    length = session["length"]
    session.clear()
    return render_template('end.html', board=board, length=length, result=result)

@web_app.route('/test')
def clear_session():
    print(session)
    print("-----------")
    session.clear()
    print(session)
    return redirect(url_for('board_new'))

@web_app.context_processor
def build_context():
    return {"auto_go": (('type' in session.keys()) and (session['type'] == 'cvc')) }



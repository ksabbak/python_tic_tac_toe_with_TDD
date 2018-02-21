import time

from flask import render_template, redirect, request, session, url_for
from tictactoe.web_app import web_app
from .route_helpers import end_conditions, render_next, build_game, start_turn, undo_board_view

@web_app.before_request
def before_request():
    if 'type' not in session and request.endpoint in ['update_board', 'ai_board', 'game_over']:
        print("Whoaaaaaaaa")
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
    session["board"] = undo_board_view(request.form["board"])
    game = start_turn(int(request.form['choice']))
    end = end_conditions(game)
    game.end_turn()
    print("Game turns: " + str(game.turn))
    if end: return end
    return render_next(game)

@web_app.route('/board')
def ai_board():
    game = start_turn()
    game.end_turn()
    end = end_conditions(game)
    print("Game turns: " + str(game.turn))
    if end: return end
    return render_next(game)

@web_app.route('/game-over')
def game_over():
    session.clear()
    # return render_template('end.html', board=board, result=result, length=length)

@web_app.route('/test')
def clear_session():
    print(session)
    print("-----------")
    session.clear()
    print(session)
    return redirect(url_for('board_new'))


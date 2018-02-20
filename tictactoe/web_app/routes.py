import time

from flask import render_template, redirect, request, session, _request_ctx_stack
from tictactoe.web_app import web_app
from tictactoe.app import Board, AI, Game
from flask.ext.session import Session


@web_app.route('/index')
@web_app.route('/')
def index():
    return redirect("/board/new")

@web_app.route('/board/new')
def board_new():
    return render_template('index.html')

@web_app.route('/board/create', methods=["POST"])
def create_board():
    session["type"] = request.form["game_type"]
    # game = _build_game(session["type"], board=request.form["board"])
    game = _build_game(board=request.form["board"])
    session["players"] = "xo"
    session["board"] = game.board.space_string()
    if game.current_player.is_ai():
        return render_template('ai_board.html', board=_board_view_builder(game.board), length=game.board.side_length())
    else:
        return render_template('board.html', board=_board_view_builder(game.board), length=game.board.side_length())
    # if session["type"] == "cvp":
    #     session["current_player"] = "player2"
    # else:
    #     session["current_player"] = "player1"
    # if session["type"][0] == "c":
    #     return render_template('ai_board.html', board=board, player=session[session["current_player"]])
    # else:
    #     return render_template('board.html', board=board)

@web_app.route('/board', methods=['POST'])
def update_board():
    game = _build_game()
    game.start_turn(int(request.form['choice']))
    session["board"] = game.board.space_string()
    end = end_conditions(game)
    game.end_turn()
    if end: return end
    if game.current_player.is_ai():
        return render_template('ai_board.html', board=_board_view_builder(game.board), length=game.board.side_length())
    else:
        return render_template('board.html', board=_board_view_builder(game.board), length=game.board.side_length())

@web_app.route('/board')
def ai_board():
    game = _build_game()
    game.start_turn()
    session["board"] = game.board.space_string()
    game.end_turn()
    end = end_conditions(game)
    if end: return end
    if game.current_player.is_ai():
        time.sleep(1)
        return render_template('ai_board.html', board=_board_view_builder(game.board), length=game.board.side_length())
    else:
        return render_template('board.html', board=_board_view_builder(game.board), length=game.board.side_length())

@web_app.route('/game-over')
def game_over(board, length, result):
    return render_template('end.html', board=board, result=result, length=length)



# @web_app.route('/test')
# def test():
#     game = Game()
#     session["test"] = game
#     game.end_turn()
#     return render_template('test.html')

# @web_app.route('/test2')
# def test2():
#     print(session['test'].turn)
#     return render_template('test2.html')


def _board_view_builder(board):
    board_view = ""
    for index, space in enumerate(board.spaces):
        if board.space_is_empty(index):
            board_view += space
        else:
            board_view += session["players"][space % 2]
    return board_view

def _build_game(board=None):
    if board is not None:
        spaces = int(board)
        moves = []
    elif session["board"] is not None:
        moves = list(session["board"])
        spaces = len(moves)
    else:
        print("panic")
    game_type = getattr(Game, session["type"])
    return game_type(spaces, moves)


def end_conditions(game):
    if game.winner() == game.current_player:
        return game_over(board=_board_view_builder(game.board), length=game.board.side_length(), result="You won! 😃")
    elif game.winner() is not None:
        return game_over(board=_board_view_builder(game.board), length=game.board.side_length(), result="You lost 😱")
    elif game.is_over():
        return game_over(board=_board_view_builder(game.board), length=game.board.side_length(), result="Game over, no one wins. 🙃")

def swap_players():
    if session["current_player"] == "player1":
        session["current_player"] = "player2"
    else:
        session["current_player"] = "player1"

from flask import render_template, redirect, request, session, _request_ctx_stack
from . import app
from ..app import Board, AI

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/board_start', methods=["POST"])
def board():
    board = Board.create_fresh_board(int(request.form["board"]))
    session["type"] = request.form["game_type"]
    session["player1"] = "x"
    session["player2"] = "o"
    session["board"] = board.space_string()
    if session["type"] == "cvp":
        session["current_player"] = "player2"
    else:
        session["current_player"] = "player1"
    if session["type"][0] == "c":
        return render_template('ai_board.html', board=board, player=session[session["current_player"]])
    else:
        return render_template('board.html', board=board)

@app.route('/board', methods=['POST'])
def update_board():
    marker = session[session["current_player"]]
    board = request.form['board']
    board = Board.create_from_existing_spaces(board)
    board.mark_space(int(request.form['choice']), marker)
    session["board"] = board.space_string()
    end = end_conditions(board, marker)
    swap_players()
    if end: return end
    if session["type"] == "pvp":
        return render_template('board.html', board=board)
    else:
        print("hi!")
        return render_template('ai_board.html', board=board, player=session[session["current_player"]])

@app.route('/board')
def ai_board():
    marker = session[session["current_player"]]
    print(marker)
    board = Board.create_from_existing_spaces(session["board"])
    ai = AI(marker)
    ai.make_move(board)
    end = end_conditions(board, "")
    swap_players()
    session["board"] = board.space_string()
    if end: return end
    if session["type"] == "cvc":
        return render_template('ai_board.html', board=board, player=session[session["current_player"]])
    else:
        return render_template('board.html', board=board)

@app.route('/game-over')
def game_over(board, result):
    return render_template('end.html', board=board, result=result)



def end_conditions(board, player_marker):
    if board.winning_marker() == player_marker:
        return game_over(board=board, result="You won! 😃")
    elif board.winning_marker() is not None:
        return game_over(board=board, result="You lost 😱")
    elif board.is_full():
        return game_over(board=board, result="Game over, no one wins. 🙃")

def swap_players():
    if session["current_player"] == "player1":
        session["current_player"] = "player2"
    else:
        session["current_player"] = "player1"

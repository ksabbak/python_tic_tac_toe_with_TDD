from flask import render_template, redirect, request, session
from . import app
# from .helpers import end_conditions
from ..app import Board, AI

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board/<int:size>')
def board(size): 
    board = Board.create_from_scratch(size)
    return render_template('board.html', board=board)

@app.route('/board', methods=['POST'])
def update_board():
    board = request.form['board']
    board = Board.create_from_existing(board)
    board.mark_space(int(request.form['choice']), "x")
    session["board"] = board.space_string()
    end = end_conditions(board, "x")
    if end: return end
    return render_template('ai_board.html', board=board)

@app.route('/board')
def ai_board():
    board = Board.create_from_existing(session["board"])
    ai = AI("o")
    ai.make_move(board)
    end = end_conditions(board, "x")
    if end: return end
    return render_template('board.html', board = board)

@app.route('/game-over')
def game_over(board, result):
    return render_template('end.html', board=board, result=result)



def end_conditions(board, player_marker):
    print(board.winning_marker())
    if board.winning_marker() == player_marker:
        return game_over(board=board, result="You won! 😃")
    elif board.winning_marker() is not None:
        return game_over(board=board, result="You lost 😱")
    elif board.is_full():
        return game_over(board=board, result="Game over, no one wins. 🙃")


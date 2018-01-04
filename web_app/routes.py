from flask import render_template, redirect, request
from . import app
from ..app import Board, AI

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/board')
def board(board=None):
    if board is not None:
        board = Board.create_from_existing(board)
    else: 
        board = Board.create_from_scratch()
    return render_template('board.html', board=board)

@app.route('/board', methods=['POST'])
def update_board():
    board = request.form['board']
    board = Board.create_from_existing(board)
    board.mark_space(int(request.form['choice']), "x")
    if board.is_full():
        return ("Game over, no one wins.")
    ai = AI("o")
    ai.make_move(board)
    if board.winning_marker() == "x":
        return ('You won!')
    elif board.winning_marker() == "o":
        return ("You lost!")
    else:
        return render_template('board.html', board=board)


@app.route('/board/<int:path>')
def three_x_three_choice(path):
    print(path)
    board = request.args.get('board')
    board = board.strip("'")
    board = Board.create_from_existing(board)
    board.mark_space(int(path), "x")
    ai = AI("o")
    ai.make_move(board)
    return three_x_three_board(board.space_string())

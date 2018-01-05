from flask import render_template, redirect, request
from . import app
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
    if board.is_full():
        return game_over(board=board, result="Game over, no one wins. 🙃")
    ai = AI("o")
    ai.make_move(board)
    if board.winning_marker() == "x":
        return game_over(board=board, result='You won! 😃')
    elif board.winning_marker() == "o":
        return game_over(board=board, result="You lost 😱")
    else:
        return render_template('board.html', board=board)

@app.route('/game-over')
def game_over(board, result):
    return render_template('end.html', board=board, result=result)

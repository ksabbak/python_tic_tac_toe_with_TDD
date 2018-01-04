from flask import render_template, redirect, url_for
from . import app
from ..app import Board

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/board')
def three_x_three_board():
    board = Board()
    return render_template('board.html', board=board)

@app.route('/board/<path:path>')
def three_x_three_choice(path):
    print(path)
    return redirect('/board')

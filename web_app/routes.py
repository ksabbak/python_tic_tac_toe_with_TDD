from flask import render_template
from . import app
from ..app import Board

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/3x3')
def three_x_three_board():
    board = Board()
    return render_template('board.html', board=board)

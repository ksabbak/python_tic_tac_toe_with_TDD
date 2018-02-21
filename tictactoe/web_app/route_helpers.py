from flask import render_template, redirect, request, session
from tictactoe.app import Game

def start_turn(move=None):
    game = build_game()
    game.start_turn(move)
    session["board"] = game.board.space_string()
    return game

def build_game(board=None):
    if board is not None:
        moves = []
        spaces = int(board)
    elif session["board"] is not None:
        moves = list(session["board"])
        spaces = len(moves)
    else:
        print("panic")
    game_type = getattr(Game, session["type"])
    return game_type(spaces, moves)

def board_view_builder(spaces):
    board_view = ""
    for space in spaces:
        if space == " ":
            board_view += space
        else:
            board_view += session["players"][int(space) % 2]
    return board_view

def undo_board_view(board_view):
    logic_board = ""
    for space in board_view:
        if space == " ":
            logic_board += space
        else:
            logic_board += str(session["players"].index(space))
    return logic_board

def render_next(game):
    if "result" in session.keys(): return redirect('/game-over')
    if game.current_player.is_ai():
        return render_template('ai_board.html', board=board_view_builder(game.board.space_string()), length=game.board.side_length())
    else:
        return render_template('board.html', board=board_view_builder(game.board.space_string()), length=game.board.side_length())

def end_conditions(game):
    session["length"] = game.board.side_length()
    if game.winner() == game.current_player:
        session["result"] = "You won! 😃"
    elif game.winner() is not None:
        session["result"] = "You lost 😱"
    elif game.is_over():
        session["result"] = "Game over, no one wins. 🙃"

def game_over(board, result, length):
    session.clear()

def take_normal_turn():
    session["board"] = undo_board_view(request.form["board"])
    return start_turn(int(request.form['choice']))

def undo_turn():
    game = build_game()
    game.undo_turn()
    session["board"] = game.board.space_string()
    return game


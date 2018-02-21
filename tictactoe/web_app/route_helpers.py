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

def _board_view_builder(board):
    board_view = ""
    for index, space in enumerate(board.spaces):
        if board.space_is_empty(index):
            board_view += space
        else:
            board_view += session["players"][space % 2]
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
    if game.current_player.is_ai():
        return render_template('ai_board.html', board=_board_view_builder(game.board), length=game.board.side_length())
    else:
        return render_template('board.html', board=_board_view_builder(game.board), length=game.board.side_length())

def end_conditions(game):
    if game.winner() == game.current_player:
        return game_over(board=_board_view_builder(game.board), length=game.board.side_length(), result="You won! 😃")
    elif game.winner() is not None:
        return game_over(board=_board_view_builder(game.board), length=game.board.side_length(), result="You lost 😱")
    elif game.is_over():
        return game_over(board=_board_view_builder(game.board), length=game.board.side_length(), result="Game over, no one wins. 🙃")

def game_over(board, result, length):
    session.clear()


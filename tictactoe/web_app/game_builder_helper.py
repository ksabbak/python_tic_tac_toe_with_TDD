from flask import render_template, redirect, request, session
from tictactoe.app import Game

class GameBuilderHelper:

    def error_handling_for_setup(self, form):
        if "game_type" not in form or "board" not in form:
            return "You must pick a board size and game type"
        if form["player1"] == "" or form["player2"] == "" :
            return "Please enter your marker choices"
        if form["player1"] == form["player2"]:
            return "The markers shouldn't match"

    def set_game_sessions(self, game, form, session=session):
        session["board"] = game.board.space_string()
        session["players"] = form['player1'] + form['player2']
        session['bgcolor'] = form['bgcolor']
        session['colors'] = [form['color1'], form['color2']]

    def build_game(self, board=None, session=session):
        if board is not None:
            moves = []
            spaces = int(board)
        elif session["board"] is not None:
            moves = list(session["board"])
            spaces = len(moves)
        else:
            return "error!"
        game_type = getattr(Game, session["type"])
        return game_type(spaces, moves)

    def board_view_builder(self, spaces, session=session):
        board_view = ""
        for space in spaces:
            if space == " ":
                board_view += space
            else:
                board_view += session["players"][int(space) % 2]
        return board_view

    def undo_board_view(self, board_view, session=session):
        logic_board = ""
        for space in board_view:
            if space == " ":
                logic_board += space
            else:
                logic_board += str(session["players"].index(space))
        return logic_board

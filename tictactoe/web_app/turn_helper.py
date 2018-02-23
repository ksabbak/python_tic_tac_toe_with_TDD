from flask import render_template, redirect, request, session
from .game_builder_helper import GameBuilderHelper

class TurnHelper:

    def start_turn(self, move=None, session=session):
        game = GameBuilderHelper().build_game(session=session)
        game.start_turn(move)
        session["board"] = game.board.space_string()
        return game

    def get_next_render_data(self, game, session=session):
        if "result" in session.keys(): return {"redirect": '/game-over'}
        session['turn'] = game.current_player.turn_order
        if game.current_player.is_ai():
            session['ai'] = True
            return {"template_name_or_list": 'ai_board.html', "board": GameBuilderHelper().board_view_builder(game.board.space_string()), "length": game.board.side_length()}
        else:
            session['ai'] = False
            return {"template_name_or_list": 'board.html', "board": GameBuilderHelper().board_view_builder(game.board.space_string()), "length": game.board.side_length()}

    def check_game_over(self, game, session=session):
        session["length"] = game.board.side_length()
        if game.winner() == game.current_player:
            session["result"] = "You won! 😃"
        elif game.winner() is not None:
            session["result"] = "You lost 😱"
        elif game.is_over():
            session["result"] = "Game over, no one wins. 🙃"

    def take_normal_turn(self, form, session=session):
        session["board"] = GameBuilderHelper().undo_board_view(request.form["board"])
        return self.start_turn(int(form['choice']))

    def undo_turn(self, session=session):
        game = GameBuilderHelper().build_game(session=session)
        game.undo_turn()
        session["board"] = game.board.space_string()
        return game

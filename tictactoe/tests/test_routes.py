from tictactoe.web_app import web_app
import flask
import unittest


class TicTacToeTestCase(unittest.TestCase):

    def setUp(self):
        web_app.testing = True
        self.app = web_app.test_client()


    def test_index(self):
        response = self.app.get('/board/new')
        assert b'<html>' in response.data

    def test_board_start_route_parameters(self):
        with web_app.test_request_context('/board/create?game_type=cvc'):
            assert flask.request.path == '/board/create'
            assert flask.request.args['game_type'] == 'cvc'

    def test_board_start_route_response_when_game_type_includes_computer(self):
        response = self.app.post('/board/create', data={'game_type': 'cvc', 'board': '9', 'player1': 'x', 'player2': 'o', 'color1': '#ffffff', 'color2': '#ffffff', 'bgcolor': '#ffffff'})
        assert b'choice' not in response.data
        assert b'Computer' in response.data

    def test_board_start_route_response_when_game_type_does_not_have_computer(self):
        response = self.app.post('/board/create', data={'game_type': 'pvp', 'board': '9', 'player1': 'x', 'player2': 'o', 'color1': '#ffffff', 'color2': '#ffffff', 'bgcolor': '#ffffff'})
        assert b'choice' in response.data
        assert b'Computer' not in response.data


    def test_ai_board_with_no_session(self):
        response = self.app.get('/board')
        assert response.status_code == 302

    def test_ai_board_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess["type"] = "cvc"
                sess["board"] = "0        "
                sess["players"] = "xo"
                sess['colors'] = ['red', 'blue']
                sess['bgcolor'] = 'white'
            response = self.app.get('/board')
            assert b'choice' not in response.data
            assert b'Computer' in response.data

    def test_board_route_update_when_human_turn(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess["type"] = "pvp"
                sess["board"] = "0        "
                sess["players"] = "xo"
                sess['colors'] = ['red', 'blue']
                sess['bgcolor'] = 'white'
            response = self.app.post('/board', data={"board": "x xo ox x", "choice": '2', "submit": "submit"})
            assert b'choice' in response.data
            assert b'Computer' not in response.data

    def test_board_route_update_when_winning_human_turn(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess["type"] = "pvp"
                sess["board"] = "0        "
                sess["players"] = "xo"
                sess['colors'] = ['red', 'blue']
                sess['bgcolor'] = 'white'
            response = self.app.post('/board', data={"board": "x xo ox x", "choice": '4', "submit": "submit"})
            assert response.status_code == 302
            assert b'game-over' in response.data



# if __name__ == '__main__':
#     unittest.main()

from tictactoe.web_app import web_app
import flask
import unittest


class TicTacToeTestCase(unittest.TestCase):

    def setUp(self):
        web_app.testing = True
        self.app = web_app.test_client()


    def test_index(self):
        response = self.app.get('/')
        assert b'<html>' in response.data

    def test_board_start_route_parameters(self):
        with web_app.test_request_context('/board_start?game_type=c'):
            assert flask.request.path == '/board_start'
            assert flask.request.args['game_type'] == 'c'

    def test_board_start_route_response_when_game_type_includes_computer(self):
        response = self.app.post('/board_start', data={'game_type': 'c', 'board': '9'})
        assert b'</form>' not in response.data

    def test_board_start_route_response_when_game_type_does_not_have_computer(self):
        response = self.app.post('/board_start', data={'game_type': 'p', 'board': '9'})
        assert b'</form>' in response.data

    def xtest_board_route_update_when_human_turn(self):
        with web_app.test_client().session_transaction() as sess:
            sess["type"] = "pvp"
            response = self.app.post('/board', data={"board": "x xo ox x", "choice": '2'})
            assert b'</form>' in response.data

    def xtest_game_over(self):
        response = self.app.get('/game-over')
        assert b'Play again?' in response.data



if __name__ == '__main__':
    unittest.main()

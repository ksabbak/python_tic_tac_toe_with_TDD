from flask import Flask
from tictactoe.config import Config


web_app = Flask(__name__)
web_app.config.from_object(Config)


from tictactoe.web_app import routes

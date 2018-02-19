import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key through the mountains'
    # SESSION_TYPE = 'redis'
    # SESSION_PERMANENT = False

import os

class Config(object):
    SECRET_KEY = os.environ.get('johanna') or 'you-will-never-guess'
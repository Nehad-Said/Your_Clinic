import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_VIEW = 'login'
    ITEMS_PER_PAGE = 10


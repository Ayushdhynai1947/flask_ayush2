import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_DIR = os.path.join(BASE_DIR, 'view')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLALCHEMY_DATABASE_DIR}/data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

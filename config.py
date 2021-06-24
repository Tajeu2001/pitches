import os
import re

class Config:
    '''
    general configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:siantayo15@localhost/pitches'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    production configuration child class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:siantayo15@localhost/pitches'



class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

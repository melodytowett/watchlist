from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
     MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
     SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    '''
    Production configuratiion child class
    '''
    pass


class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
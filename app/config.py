from distutils.debug import DEBUG


class Config:
    pass

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

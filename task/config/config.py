import os

class BaseConfig:
    """Base config vars."""
    HOST = "127.0.0.1"
    PORT = 5000
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_HOST', 'sqlite://')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    HOST = "0.0.0.0"

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    
import os 

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
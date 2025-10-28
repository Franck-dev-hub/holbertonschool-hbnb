import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "dev_secret_key123"
    SQLALCHEMY_DATABASE_URI = "sqlite://development.db"
    SQLALCHEMY_TRACK_MODIFICATION = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

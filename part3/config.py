import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = [
        "http://localhost:5000",
        "http://127.0.0.1:5000",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "null"
    ]


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "dev_secret_key123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///development.db"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

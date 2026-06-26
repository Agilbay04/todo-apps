import os


class DbConfig:
    DB_PROVIDER = os.environ.get('DB_PROVIDER', 'postgresql')
    DB_USER = os.environ.get('DB_USER')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')

    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    SQLALCHEMY_DATABASE_URI = (
        f"{DB_PROVIDER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

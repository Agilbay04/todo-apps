import os


class AppConfig:
    APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')
    APP_PORT = int(os.environ.get('APP_PORT', 5005))
    APP_ENV = os.environ.get('APP_ENV', 'dev')

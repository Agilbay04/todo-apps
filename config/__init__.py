from dotenv import load_dotenv

load_dotenv()

from config.app import AppConfig
from config.db import DbConfig


class Config(AppConfig, DbConfig):
    pass

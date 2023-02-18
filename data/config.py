"""Модуль настроек подключений"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from environs import Env
from loguru import logger


@dataclass
class DbConfig(ABC):

    @abstractmethod
    def get_url(self):
        pass


@dataclass
class DbSqlLiteConfig(DbConfig):
    db_name: str

    def get_url(self):
        return f"sqlite:///{self.db_name}"


@dataclass
class DbPGConfig(DbConfig):
    host: str
    password: str
    port: int
    user: str
    db_name: str

    def get_url(self):
        # 'postgresql+psycopg2://user:password@hostname:port/database_name'
        return f'postgresql+pyscopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


class ConfigSingleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, path: str):
        self.path = path
        self.env = Env()
        self.env.read_env(self.path)
        self.__tg_bot = TgBot(
            token=self.env.str("BOT_TOKEN"),
            admin_ids=list(map(int, self.env.list("ADMINS")))
        )
        self.__db = DbSqlLiteConfig(db_name="POsparTU_DB")

    @property
    def tg_bot(self):
        return self.__tg_bot

    @property
    def db(self):
        return self.__db


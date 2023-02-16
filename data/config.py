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


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig | None


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    tg_bot = TgBot(
        token=env.str("BOT_TOKEN"),
        admin_ids=list(map(int, env.list("ADMINS")))
    )
    db = DbSqlLiteConfig(db_name='POsparTU_DB')

    config = Config(
        tg_bot=tg_bot,
        db=db
    )
    return config

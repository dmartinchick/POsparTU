"""Модуль настроек подключений"""

from dataclasses import dataclass
from environs import Env
from loguru import logger


# Глобальные перемееные
FORMAT = '%(asctime)-15s: %(message)s'


@dataclass
class DbConfig:
    pass


@dataclass
class DbPGConfig(DbConfig):
    host: str
    password: str
    port: int
    user: str
    db_name: str


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

    config = Config(
        tg_bot=tg_bot,
        db=None
    )
    return config

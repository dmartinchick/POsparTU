from loguru import logger
from aiogram import Bot, Dispatcher, executor, types

from data.config import load_config


def main():
    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot)


if __name__ == '__main__':
    main()

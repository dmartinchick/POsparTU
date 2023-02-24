from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import logger, ConfigSingleton
from handlers.echo import register_echo_handlers
from handlers.main_menu import register_main_menu_handlers
from handlers.admin_panel import register_admin_panel_handlers

from utils.other import created_all, add_user, update_user


@logger.catch
def main():
    config = ConfigSingleton(path='.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # register handlers
    register_echo_handlers(dp)
    register_main_menu_handlers(dp)
    register_admin_panel_handlers(dp)

    # start program
    executor.start_polling(dp)


if __name__ == '__main__':
    main()

from data.config import logger
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import load_config
from handlers.echo import register_echo_handlers
from handlers.main_menu import register_main_menu_handlers
from handlers.admin_panel import register_admin_panel_handlers


@logger.catch
def main():
    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # register handlers
    register_echo_handlers(dp)
    register_main_menu_handlers(dp)
    register_admin_panel_handlers(dp)

    executor.start_polling(dp)


if __name__ == '__main__':
    main()

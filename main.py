from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import logger, ConfigSingleton
from handlers.echo import register_echo_handlers
from handlers.main_menu import register_main_menu_handlers
from handlers.admin_panel import register_admin_panel_handlers
from db.containers import Container

from db.user.commands import get_superusers_list, get_all_active_users, get_user_by_id, add_new_user
# TODO: Для тестов
from db.user.model import User


@logger.catch
def main():
    config = ConfigSingleton(path='.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    container = Container()

    # register handlers
    register_echo_handlers(dp)
    register_main_menu_handlers(dp)
    register_admin_panel_handlers(dp)

    # start program

    executor.start_polling(dp)


if __name__ == '__main__':
    main()

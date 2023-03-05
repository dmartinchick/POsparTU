from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import logger, ConfigSingleton
from handlers.echo import register_echo_handlers
from handlers.main_menu import register_main_menu_handlers
from handlers.admin_panel import register_admin_panel_handlers
from db.containers import Container
from utils.notifi_admins import on_startup_notify, on_shutdown_notify

from db.user.commands import get_superusers_list, get_all_active_users, get_user_by_id, add_new_user
# TODO: Для тестов
from db.user.model import User


async def on_startup(dp: Dispatcher):
    container = Container()
    await on_startup_notify(dp, container=container)


async def on_shutdown(dp: Dispatcher):
    container = Container()
    await on_shutdown_notify(dp, container)


@logger.catch
def main():
    config = ConfigSingleton(path='.env')
    bot = Bot(token=config.tg_bot.token)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    # container = Container()

    # register handlers
    register_echo_handlers(dp)
    register_main_menu_handlers(dp)
    register_admin_panel_handlers(dp)

    # start program

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == '__main__':
    main()

from data.config import logger
from aiogram import Dispatcher
from db.user.commands import get_superusers_list
from db.containers import Container


async def on_startup_notify(dp: Dispatcher, container: Container):
    superusers = get_superusers_list(container)
    for user in superusers:
        try:
            await dp.bot.send_message(user.id, "🛎\t\tБот запущен")
        except Exception as err:
            logger.exception(err)


async def on_shutdown_notify(dp: Dispatcher, container: Container):
    superusers = get_superusers_list(container)
    for user in superusers:
        try:
            await dp.bot.send_message(user.id, "🛎\t\tБот отключён")
        except Exception as err:
            logger.exception(err)

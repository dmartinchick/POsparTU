from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            BotCommand('menu', 'Показать главное меню'),
            BotCommand('start', "Запуск бота"),
            BotCommand('help', "Вызов справки"),
            BotCommand('admin_panel', "Вызов панули администратора")
        ]
    )

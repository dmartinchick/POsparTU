from aiogram.types import Message
from aiogram import Dispatcher


async def echo(message: Message):
    await message.answer(message.text)


def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)

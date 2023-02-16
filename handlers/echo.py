from aiogram.types import Message
from aiogram import Dispatcher

from data.config import logger


async def echo(message: Message):
    logger.info(message.text)
    await message.answer(message.text)


def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)

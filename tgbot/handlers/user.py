from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(m: Message):
    await m.answer(f"Привет, {m.from_user.get_mention(m.from_user.first_name)}")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

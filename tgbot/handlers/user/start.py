from aiogram.types import Message


async def start_handler(
        m: Message
):

    await m.answer(
        text="Добро пожаловать в бота!"
    )
from aiogram import Dispatcher

from tgbot.handlers.user.start import start_handler


def register_user(dp: Dispatcher):

    dp.register_message_handler(
        start_handler,
        commands=['start'],
        state='*'
    )
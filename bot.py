import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from sqlalchemy.engine import URL

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.user import register_user

from tgbot.middlewares.db import DbMiddleware
from tgbot.models.database.base import Database

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_user(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',

    )
    logger.info("Starting bot")
    config = load_config(".env")

    if config.tg_bot.use_redis:
        storage = RedisStorage2(config.tg_bot.redis_host)
    else:
        storage = MemoryStorage()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    db = Database()
    await db.create_pool(
        URL(
            drivername="postgresql+asyncpg",
            username=config.db.user,
            password=config.db.password,
            host=config.db.host,
            database=config.db.database,
            query={},
            port=5432
        )
    )

    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config
    bot['pool'] =db.pool

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

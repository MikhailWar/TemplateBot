from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    async def pre_process(self, obj, data, *args):
        pool = obj.bot.get('pool')
        data['session'] = pool()
        # Передаем данные из таблицы в хендлер
        # data['some_model'] = await Model.get()

    async def post_process(self, obj, data, *args):

        if session:=data.get("session"):
            await session.close()
            data.pop('session')

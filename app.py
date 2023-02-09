from aiogram import executor
from handlers.user.start import start, pinger_7
from loader import dp


async def on_startup(dispatcher):
    await start(dispatcher)
    await pinger_7(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
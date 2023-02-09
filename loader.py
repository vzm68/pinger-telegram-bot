from aiogram import Bot, Dispatcher, types

from data import config
import logging

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(filename=config.log_path, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
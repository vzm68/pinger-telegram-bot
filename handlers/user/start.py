import asyncio
import logging

import ping3
from datetime import datetime

from aiogram import Dispatcher
from data.config import chat_id, group_id, ip_list, login
from exe.tail_log import tail_log


async def start(dp: Dispatcher):
    await dp.bot.send_message(text=f'Бот запущено успішно!\n\n📝Останні логи:\n<code>{"▪".join(tail_log())}</code>'
                              , chat_id=chat_id)


def diff_dates(date, login):
    """
    Receives time when link down,
    and calculates the difference between the current time
    (when the link went up).
    :param date:
    Gets time type "%Y-%m-%d %H:%M"(2023-02-03 14:30)
    :param login:
    Gets login from parent functions.
    :return:
    the difference between the current time (when the link went up).
    """
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M')
    date1 = datetime.strptime(date, '%Y-%m-%d %H:%M')
    date2 = datetime.strptime(date_now, '%Y-%m-%d %H:%M')
    delta = date2 - date1
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    logging.info(f"Connection is back at {date_now}. Time of absence {days} days, {hours} hours, {minutes} minutes.")
    if days > 0:
        return f"{login}\n\n" \
               f"Link has been return 🥳\n"\
               f"Was down <b>{days}</b> days, <b>{hours}</b> hours, <b>{minutes}</b> minutes😵"
    elif hours > 0:
        return f"{login}\n\n" \
               f"Link has been return 🥳\n"\
               f"Was down <b>{hours}</b> hours, <b>{minutes}</b> minutes🙄"
    else:
        return f"{login}\n\n" \
               f"Link has been return 🥳\n"\
               f"Was down <b>{minutes}</b> minutes🗿"


async def pinger_7(dp: Dispatcher, time=''):
    while True:
        for ip in ip_list:
            response = ping3.ping(ip)
            if response is not False and response is not None:
                ip_list[ip][1] = 0
                if ip_list[ip][0] is False:
                    ip_list[ip][0] = True
                    await dp.bot.send_message(text=f'{diff_dates(time, login)}', chat_id=group_id)
            else:
                if ip_list[ip][1] >= 3:
                    continue
                else:
                    ip_list[ip][1] += 1
                if ip_list[ip][0] is True and ip_list[ip][1] == 3:
                    ip_list[ip][0] = False
                    await dp.bot.send_message(text=f'{login}\n\n🌐 Lost connection :(', chat_id=group_id)
                    time = datetime.now().strftime('%Y-%m-%d %H:%M')
                    logging.info(f"Lost connection at {time}")
        await asyncio.sleep(1)
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from datetime import datetime, time

# Ваш токен бота
TOKEN = 'BOT_TOKEN'

# Создаем экземпляр бота
bot = Bot(token=TOKEN)

# Создаем экземпляр диспетчера
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def send_daily_message():
    chat_id = "CHAT_ID" # ID чата, куда будем отправлять сообщение
    message = "YOUR_MESSAGE "  # Текст сообщения
    await bot.send_message(chat_id=chat_id, text=message)


# Задаем время, когда будет отправляться сообщение
send_time = time(hour=12, minute=00, second=0)


# Запускаем бесконечный цикл, который проверяет текущее время и отправляет сообщение, если оно соответствует заданному времени
async def scheduler():
    while True:
        now = datetime.now().time()
        weekday = datetime.now().weekday()
        if now.hour == send_time.hour and now.minute == send_time.minute and now.second == send_time.second and weekday == 3:
            await send_daily_message()
        elif now.hour == send_time.hour and now.minute == send_time.minute and now.second == send_time.second and weekday == 4:
            await send_daily_message()
        elif now.hour == send_time.hour and now.minute == send_time.minute and now.second == send_time.second and weekday == 5:
            await send_daily_message()
            await asyncio.sleep(1)


# Создаем команду для запуска бота
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Bot started!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp, loop=loop, skip_updates=True)

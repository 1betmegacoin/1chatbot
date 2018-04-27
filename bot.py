import asyncio
import logging
import constants

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token=constants.TOKEN, loop=loop)
dp = Dispatcher(bot)


# wtf python 3.6.4 :)
# konstanti bolshimi pishutsa :) Запомню) спасибо pizdit :) python normalnii )

@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_new_members(message: types.Message):
    for user in message.new_chat_members:
        await bot.restrict_chat_member(message.chat.id, user.id)

    await message.delete()


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def member_left(message: types.Message):
    await message.delete()

# otkroi gruppu
@dp.message_handler(regexp='ping')
async def ping_pong(message: types.Message):
    await message.reply('pong')


if __name__ == '__main__':
    start_polling(dp, loop=loop, skip_updates=True)

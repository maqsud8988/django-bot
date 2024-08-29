from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from django.conf import settings
from bot.models import TgUser

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Xush kelibsiz!")
    try:
        user = await TgUser.objects.aget(user_id=message.from_user.id)
    except TgUser.DoesNotExist:
        user = await TgUser.objects.acreate(user_id=message.from_user.id)

    await message.reply(f"Salom {user.name}")



def start_bot():
    executor.start_polling(dp, skip_updates=True)

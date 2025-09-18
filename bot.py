from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# Токен бота (добавляется в Render → Environment Variables)
API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Добавь его в переменные окружения Render.")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Ссылка на твой Colab
COLAB_LINK = "https://colab.research.google.com/drive/1ywFn2Tw8jCONAaFC_3dcUTA___ydARbn?usp=sharing"

@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("🚀 Открыть Colab", url=COLAB_LINK)
    )
    await message.reply(
        "Привет! Я бот для команды 🎧\n\n"
        "Жми на кнопку, чтобы открыть свой Colab с кодом для расшифровки:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

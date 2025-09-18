# Telegram Bot (Render + Aiogram)

Этот бот показывает кнопку со ссылкой на Google Colab, где можно запустить код для расшифровки аудио через Whisper.

## 🚀 Деплой на Render

1. Склонируй репозиторий или сделай Fork.
2. Зайди на [Render](https://render.com/), создай **Web Service**.
3. В настройках укажи:
   - **Environment** → Python 3
   - **Build Command** → `pip install -r requirements.txt`
   - **Start Command** → `python bot.py`
4. В разделе **Environment Variables** добавь:
   - Key: `BOT_TOKEN`
   - Value: токен твоего бота из BotFather
5. Запусти сервис → бот будет работать 24/7 🎉

## 🔧 Дополнительно

Добавлен файл `runtime.txt`, чтобы Render использовал Python 3.10 (иначе aiogram не собирается на Python 3.13).

# Telegram Bot (Railway + Aiogram)

Этот бот показывает кнопку со ссылкой на Google Colab, где можно запустить код для расшифровки аудио через Whisper.

## 🚀 Деплой на Railway

1. Скачай или fork проекта в GitHub.
2. Перейди на [Railway](https://railway.app/), создай **New Project → Deploy from GitHub repo**.
3. Укажи свой репозиторий с этим кодом.
4. Railway автоматически увидит `runtime.txt` и возьмет Python 3.10.
5. В настройках проекта добавь переменную окружения:
   - Key: `BOT_TOKEN`
   - Value: токен твоего бота из BotFather
6. Запусти Deploy → бот будет работать 24/7 🎉

## 🔧 Команды Railway
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python bot.py`

# Telegram Bot на Fly.io

Этот бот показывает кнопку со ссылкой на Google Colab, где можно запустить код для расшифровки аудио через Whisper.

## 🚀 Деплой через GitHub Codespaces (без установки на ПК)

1. Склонируй репозиторий на GitHub.  
2. В GitHub → Code → Codespaces → Create Codespace.  
3. В терминале Codespaces выполни команды:

```bash
curl -L https://fly.io/install.sh | sh
export PATH=$HOME/.fly/bin:$PATH

fly auth login
fly launch --no-deploy
fly secrets set BOT_TOKEN=твой_токен
fly deploy
```

4. Через минуту бот будет работать 24/7 на Fly.io.

---
⚡ Бесплатный план Fly.io даёт достаточно ресурсов для простого Telegram-бота.

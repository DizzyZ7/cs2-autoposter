import os
import asyncio
from aiogram import Bot
from aiogram.exceptions import TelegramAPIError

# Получаем токен бота и список каналов/тем
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGETS = os.getenv("TARGETS")

# Текст для публикации
MESSAGE_TEXT = """
🚀 Верификация на Youpin898 и Buff163 стала возможна!  

Подтвердите свой аккаунт безопасно и быстро, чтобы пользоваться всеми преимуществами платформ:  

✔️ После верификации вы получаете:
- 🔐 Надёжную защиту аккаунта  
- ⚡ Быстрый доступ к торговле и предметам  
- 💎 Полный функционал платформ без ограничений  
- 🌐 Поддержку валют и языков  
- 📈 Удобный интерфейс для обмена  

💰 Стоимость верификации: 80 USDT  
💳 Оплата через TRC20  

✍️ Для верификации обращайтесь напрямую: [@DizZy_Z7](https://t.me/DizZy_Z7) ✅

Не тратьте время на ручную проверку — всё официально и безопасно!
"""

async def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN не задан!")
        return

    if not TARGETS:
        print("❌ TARGETS не задан!")
        return

    targets_list = [t.strip() for t in TARGETS.strip().split("\n") if t.strip()]
    if not targets_list:
        print("❌ Нет ни одной группы в TARGETS!")
        return

    async with Bot(token=BOT_TOKEN) as bot:
        for item in targets_list:
            try:
                if ":" in item:
                    chat_id, thread_id = item.split(":")
                    await bot.send_message(
                        chat_id=chat_id.strip(),
                        text=MESSAGE_TEXT.strip(),
                        reply_to_message_id=int(thread_id.strip()),
                        disable_web_page_preview=False
                    )
                    print(f"✅ Сообщение отправлено в {chat_id} (тема {thread_id})")
                else:
                    await bot.send_message(
                        chat_id=item.strip(),
                        text=MESSAGE_TEXT.strip(),
                        disable_web_page_preview=False
                    )
                    print(f"✅ Сообщение отправлено в {item}")
            except TelegramAPIError as e:
                print(f"❌ Ошибка при отправке в {item}: {e}")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import os
from aiogram import Bot
from aiogram.exceptions import TelegramAPIError


MESSAGE_TEXT = """
🚨 Это реально произошло! 🚨
После долгого ожидания игроки и трейдеры получили то, чего так не хватало — удобный сервис сделанный людьми, которые шарят за CS2 🎮💣

Мой реферальный код👇
https://csboard.trade?ref=I9THBZPO

🗑️ Прощаемся с кучей скринов в личке
🔍 Больше не нужно вручную выискивать нужный айтем

🧠 Всё работает элементарно:
✍️ Вводишь название предмета → 📦 находишь нужный вариант → 🔄 меняешься без лишней суеты

🛠️ Функционал уже на старте:
💎 Поиск идёт по предметам, а не по никам и скринам
💰 Цены обновляются и отображаются в разных валютах
🌐 Поддержка нескольких языков — комфорт для всех регионов
🔐 Вход через Google или Steam — быстро и безопасно 🛡️

🎉 И это ещё не всё!
В Telegram-канале проекта прямо сейчас разыгрывают нож 🔪🗡️ — https://t.me/csboardtrade/11 🎁🔥

Но и это еще не всё ❌
Между своими рефералаами я разыграю дополнительно ножик, так что не упусти возможность 😎

Залетай, смотри, пробуй — трейдить в CS2 стало проще 🚀💥
"""


def load_groups():
    groups = []
    index = 1

    while True:
        chat_id = os.getenv(f"CHANNEL_ID_{index}")
        thread_id = os.getenv(f"THREAD_ID_{index}")

        if not chat_id:
            break

        groups.append({
            "chat_id": chat_id,
            "thread_id": int(thread_id) if thread_id and thread_id.strip() else None
        })

        index += 1

    return groups


async def send_message(bot: Bot, chat_id: str, thread_id: int | None):
    try:
        if thread_id:
            await bot.send_message(
                chat_id=chat_id,
                text=MESSAGE_TEXT.strip(),
                message_thread_id=thread_id
            )
            print(f"✅ Отправлено в {chat_id} (тема {thread_id})")
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=MESSAGE_TEXT.strip()
            )
            print(f"✅ Отправлено в {chat_id} (обычный чат)")
    except TelegramAPIError as e:
        print(f"❌ Ошибка в {chat_id}: {e}")


async def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        print("❌ BOT_TOKEN не найден")
        return

    groups = load_groups()

    if not groups:
        print("❌ Нет настроенных групп")
        return

    async with Bot(token=token) as bot:
        tasks = [
            send_message(bot, group["chat_id"], group["thread_id"])
            for group in groups
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

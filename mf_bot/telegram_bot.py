import logging
from aiogram import Bot, Dispatcher, types

from settings import TELEGRAM_API_TOKEN


ALL_MESSAGES = []
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_all_text_messages(message: types.Message) -> None:
    if message.text:
        ALL_MESSAGES.append({'chat_id': message.chat.id,
                             'username': message.from_user.full_name,
                             'message': message.text})


async def get_last_message() -> dict | None:
    try:
        return ALL_MESSAGES[-1]
    except IndexError:
        return None


async def run_bot() -> None:
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

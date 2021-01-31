from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, CallbackQuery
from aiogram.utils.markdown import text, bold


API_TOKEN = '1225000795:AAEPaeVjyJceIiPOXXhvmueUm-yf6oY6VWE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


"""Обработчик команд"""


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message) -> None:
    """Отправляет приветственное сообщение и помощь по боту"""
    first_msg = text(bold("Привет"))
    await message.answer(first_msg, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

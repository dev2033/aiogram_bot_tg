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
    with open('music.mp3', "rb") as m:
        music = m.read()
    await bot.send_audio(message.chat.id, audio=music, title='Отражение',
                         performer='Король и Шут')
    with open('main.txt', 'rb') as file:
        doc = file.read()
    await bot.send_document(message.chat.id, document=doc)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import os

TOKEN=os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp=Dispatcher()
logging.basicConfig(filename="logs.log",level=logging.INFO, format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
@dp.message(Command(commands=['start','lets_go']))
async def process_command_start(message:Message):
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    text= f"Привет, {user_name}!"
    logging.info(f'{user_name} c {user_id} запустил бота')
    await bot.send_message(chat_id=user_id,text=text)


@dp.message()
async def send_echo(message:Message):
    alphabet_dict = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
    ' ': ' '
    }
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    text=[]
    for el in message.text:
        if el in alphabet_dict.keys():
            char=alphabet_dict[el]
        else:
            char=alphabet_dict.get(el.upper(),"?").lower()
            logging.warning("Неизвестный символ - {}".format(el))
        text.append(char)
    text="".join(text)
    logging.info(f'{user_name} c {user_id} отправил {text}')
    await message.answer(text=text)

if __name__=="__main__":
    dp.run_polling(bot)
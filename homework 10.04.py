import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token="7161846829:AAEcozQpBztwMJ0ntcypIAD3oNHkiIH6s4w")
# Диспетчер
dp = Dispatcher()

def return_list(list):   # це потрібно для того щоб красиво виводити список
    a = str()
    for i in list:
        a += i.replace("[""]""'", "")
        if not i == list[-1]:
            a += ", "
    return a


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("/help - отримати довідку за командами\n/start - Написати Hello World!\n/roll - рандомне число від 1 до 100")

    #await bot.send_message(chat_id= message.chat.id, text='Help message')
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    for i in range(100):
        await message.answer("Hello World!")


@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        if len(args) == 1:
            await message.answer(f"Випадкове число від 1 до {args[0]}: {random.randint(1, int(args[0]))}")
        elif len(args) == 2:
            await message.answer(f"Випадкове число від {args[0]} до {args[1]}: {random.randint(int(args[0]), int(args[1]))}")
        elif len(args) > 2:
            await message.answer(f"Випадкове число з списку {return_list(args)}: {random.choice(args)}")
    else:
        await message.answer(f"Випадкове число від 1 до 100: {random.randint(1, 100)}")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
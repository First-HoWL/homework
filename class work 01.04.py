import random
import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class SumStates(StatesGroup):
    first_number = State()
    second_number = State()
    znak_number = State()


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token="7161846829:AAEcozQpBztwMJ0ntcypIAD3oNHkiIH6s4w")
# Диспетчер
dp = Dispatcher()


def return_list(list):
    a = str()
    for i in range(len(list)):
        a += str(list[i]).replace("[""]""'", "")
        if not i == (len(list) - 1):
            a += ", "
    a += "."
    return a


def disney_return_list(list):
    a = str()
    if len(list) == 0:
        return '---'
    for i in range(len(list)):
        a += str(list[i]).replace("[""]""'", "")
        a += '\n'
    return a


@dp.message(Command("random_disney_person"))
async def cmd_random_disney_person(message: types.Message):
    page = random.randint(1, 7438)
    url = f'https://api.disneyapi.dev/character?pageSize=1&page={page}'
    response = requests.get(url)
    currensies_data = response.json()['data']
    if response.ok:
        await message.answer(
            f"Ім\'я: {currensies_data['name']}"
            f"\nФільми:\n{disney_return_list(currensies_data['films'])}"
            f"\nКороткі фильми:\n{disney_return_list(currensies_data['shortFilms'])}"
            f"\nТВ-шоу:\n{disney_return_list(currensies_data['tvShows'])}"
            f"\nІгри:\n{disney_return_list(currensies_data['videoGames'])}")




@dp.message(Command("sum"))
async def cmd_sum(message: types.Message, state: FSMContext):
    await message.answer('Введіть перше число:')
    await state.set_state(SumStates.first_number)


@dp.message(SumStates.first_number)
async def cmd_first_number(message: types.message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return

    await state.update_data(first_number=message.text)
    await message.answer('Введіть друге число:')
    await state.set_state(SumStates.second_number)


@dp.message(SumStates.second_number)
async def cmd_second_number(message: types.message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return

    await state.update_data(second_number=message.text)
    await message.answer('Введіть арифметичний знак:')
    await state.set_state(SumStates.znak_number)


@dp.message(SumStates.znak_number)
async def cmd_znak_number(message: types.message, state: FSMContext):
    if message.text not in ['+', '/', '-', '*']:
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return
    first_number = (await state.get_data())['first_number']
    second_number = (await state.get_data())['second_number']
    znak_number = message.text
    await state.clear()
    if znak_number == '+':
        await message.answer(f"{first_number} {znak_number} {second_number} = {int(first_number) + int(second_number)}")
    elif znak_number == '*':
        await message.answer(f"{first_number} {znak_number} {second_number} = {int(first_number) * int(second_number)}")
    elif znak_number == '/':
        await message.answer(f"{first_number} {znak_number} {second_number} = {int(first_number) / int(second_number)}")
    elif znak_number == '-':
        await message.answer(f"{first_number} {znak_number} {second_number} = {int(first_number) - int(second_number)}")





@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/help - отримати довідку за командами"
        "\n/start - Написати Hello World!"
        "\n/roll - випадкове число від 1 до 100"
        "\n/roll - (до)випадкове число від 1 до введенного числа"
        "\n/roll - (від)(до) випадкове число від першого числа до другого числа"
        "\n/roll - (число) (число) (число)... - випадковий параметр"
        "\n/sum - арифметичні дії"
        "\n/random_list - (від)(до)(кількість)випадковий список чисел"
        "\n/random_disney_person - вивести випадкового персонажу Дісней")


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
            await message.answer(
                f"Випадкове число від {args[0]} до {args[1]}: {random.randint(int(args[0]), int(args[1]))}")
        elif len(args) > 2:
            await message.answer(f"Випадкове число з списку {return_list(args)}: {random.choice(args)}")
    else:
        await message.answer(f"Випадкове число від 1 до 100: {random.randint(1, 100)}")


@dp.message(Command("random_list"))
async def cmd_random_list(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        if len(args) == 3:
            random_list = [random.randint(int(args[0]), int(args[1])) for i in range(int(args[2]))]
            await message.answer(
                f"Випадковий список від {args[0]} до {args[1]}, {args[2]} - символів: {return_list(random_list)}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
import random
import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


class SumStates(StatesGroup):
    first_number = State()
    second_number = State()
    znak_number = State()


class ButtonStates(StatesGroup):
    choose_button = State()


class CounterStates(StatesGroup):
    ChooseButton = State()


class ValutStates(StatesGroup):
    FirstValut = State()
    SecondValut = State()
    AmountValut = State()


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7161846829:AAEcozQpBztwMJ0ntcypIAD3oNHkiIH6s4w")
# Диспетчер
dp = Dispatcher()
# https://t.me/Cucumber_s_Bot - мой бот



@dp.message(Command("kurs_valut"))
async def cmd_kyrs_valut(message: types.Message, state: FSMContext):
    await message.answer('Введіть першу валюту:')
    await state.set_state(ValutStates.FirstValut)


@dp.message(ValutStates.FirstValut)
async def cmd_first_valut_choose(message: types.message, state: FSMContext):
    address = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/'
    first_url = f"{address}currencies.json"
    currensies_response = requests.get(first_url)
    currensies_list = list(currensies_response.json().keys())
    currency_from = message.text
    if currency_from not in currensies_list:
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return
    await state.update_data(Currensies_List=currensies_list)
    await state.update_data(Currensies_From=currency_from)
    await message.answer('Введіть другу валюту:')
    await state.set_state(ValutStates.SecondValut)


@dp.message(ValutStates.SecondValut)
async def cmd_second_valut_choose(message: types.message, state: FSMContext):
    currensies_list = (await state.get_data())['Currensies_List']
    currency_to = message.text
    if currency_to not in currensies_list:
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return
    await state.update_data(Currensies_To=currency_to)
    await message.answer('Введіть кількість:')
    await state.set_state(ValutStates.AmountValut)


@dp.message(ValutStates.AmountValut)
async def cmd_second_valut_choose(message: types.message, state: FSMContext):
    currency_from = (await state.get_data())['Currensies_From']
    currency_to = (await state.get_data())['Currensies_To']
    amount = message.text
    if not amount.isnumeric():
        await message.answer('Ви ввели некоректне значення! Спробуйте ще раз.')
        return

    address = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/'
    url = f'{address}currencies/{currency_from}.json'
    response = requests.get(url)

    if not response.ok:
        await message.answer('Щось пішло не так')
    as_json = response.json()[currency_from]
    rate = as_json[currency_to]
    await message.answer(f"{amount} {currency_from} = {round(rate * int(amount), 2)} {currency_to}")
    await state.clear()

# ---random_disney_person---


def disney_return_list(lists):
    a = str()
    if len(lists) == 0:
        return '---'
    for i in range(len(lists)):
        a += str(lists[i]).replace("[""]""'", "")
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
            f"Ім\'я: {currensies_data['name']}\n\n"
            f"Фільми:\n{disney_return_list(currensies_data['films'])}\n"
            f"Короткі фильми:\n{disney_return_list(currensies_data['shortFilms'])}\n"
            f"ТВ-шоу:\n{disney_return_list(currensies_data['tvShows'])}\n"
            f"Ігри:\n{disney_return_list(currensies_data['videoGames'])}")

# ---Sum---


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

# ---Buttons---


@dp.message(Command("buttons"))
async def cmd_buttons(message: types.Message, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text='Button 1!'), types.KeyboardButton(text='Button 2!'))
    builder.row(types.KeyboardButton(text='Button 3!'), types.KeyboardButton(text='Button 4!'))
    builder.row(types.KeyboardButton(text='Button 5!'), types.KeyboardButton(text='Button 6!'))

    # keybord = types.ReplyKeyboardMarkup(
    #     keyboard=[
    #         [types.KeyboardButton(text='Button 1!'), types.KeyboardButton(text='Button 2!')],
    #         [types.KeyboardButton(text='Button 3!'), types.KeyboardButton(text='Button 4!')],
    #         [types.KeyboardButton(text='Button 5!'), types.KeyboardButton(text='Button 6!')]
    #     ],
    #     resize_keyboard=True
    # )

    await message.answer('Тут будуть кнопки!', reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(ButtonStates.choose_button)


@dp.message(ButtonStates.choose_button)
async def onclick_button_1(message: types.Message, state: FSMContext):
    if message.text in ['Button 1!', 'Button 2!', 'Button 3!', 'Button 4!', 'Button 5!', 'Button 6!']:
        await message.answer(f'Bи натиснули на кнопку {message.text}', reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.answer('Натисніть на кнопку!')

# ---Inline_Buttons---


def get_buttons_keybord():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='Button 1', callback_data='button_1'),
                types.InlineKeyboardButton(text='Button 2', callback_data='button_2'))
    builder.row(types.InlineKeyboardButton(text='Google', url='https://www.google.com'))
    return builder


@dp.message(Command("inline_buttons"))
async def cmd_inline_button(message: types.Message):
    await message.answer('Оберіть дію', reply_markup=get_buttons_keybord().as_markup())


@dp.callback_query(F.data == 'button_1')
async def button_1_callback(callback: types.CallbackQuery):
    # await callback.message.answer('Ви натиснули кнопку Button 1!')
    await callback.message.edit_text('Ви натиснули кнопку Button 1!', reply_markup=get_buttons_keybord().as_markup())
    await callback.answer(text='Ви натиснули кнопку Button 1!', show_alert=True)
    await callback.answer()


@dp.callback_query(F.data == 'button_2')
async def button_1_callback(callback: types.CallbackQuery):
    # await callback.message.answer('Ви натиснули кнопку Button 2!')
    await callback.message.edit_text('Ви натиснули кнопку Button 2!', reply_markup=get_buttons_keybord().as_markup())
    await callback.answer(text='Ви натиснули кнопку Button 2!', show_alert=True)
    await callback.answer()

# ---Bot_Counter---


def get_buttons_counter_keybord():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='+ 1', callback_data='+1'),
                types.InlineKeyboardButton(text='- 1', callback_data='-1'),
                types.InlineKeyboardButton(text='Stop', callback_data='stop'))
    return builder


@dp.message(Command("counter"))
async def cmd_counter(message: types.Message, state: FSMContext):
    znachenya = int(0)
    await state.update_data(Znacheniya=znachenya)
    await message.answer(f'Поточне значення: {znachenya}!', reply_markup=get_buttons_counter_keybord().as_markup())


@dp.callback_query(F.data == '+1')
async def button_1_counter_callback(callback: types.CallbackQuery, state: FSMContext):
    znachenya = (await state.get_data())['Znacheniya']
    znachenya += 1
    await state.update_data(Znacheniya=znachenya)
    await callback.message.edit_text(f'Поточне значення: {znachenya}!',
                                     reply_markup=get_buttons_counter_keybord().as_markup())
    await callback.answer()


@dp.callback_query(F.data == '-1')
async def button_1_counter_callback(callback: types.CallbackQuery, state: FSMContext):
    znachenya = (await state.get_data())['Znacheniya']
    znachenya -= 1
    await state.update_data(Znacheniya=znachenya)
    await callback.message.edit_text(f'Поточне значення: {znachenya}!',
                                     reply_markup=get_buttons_counter_keybord().as_markup())
    await callback.answer()


@dp.callback_query(F.data == 'stop')
async def button_1_counter_callback(callback: types.CallbackQuery, state: FSMContext):
    znachenya = (await state.get_data())['Znacheniya']
    await callback.message.edit_text(f"Итого: {znachenya}")
    await callback.answer()

# ---Help---


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/help - отримати довідку за командами"
        "\n/start - Написати Hello World!"
        "\n/roll - випадкове число від 1 до 100"
        "\n/roll - (до) - випадкове число від 1 до введенного числа"
        "\n/roll - (від)(до) - випадкове число від першого до другого числа"
        "\n/roll - (число) (число) (число)... - випадковий параметр"
        "\n/sum - арифметичні дії"
        "\n/random_list - (від)(до)(кількість)випадковий список чисел"
        "\n/buttons - кнопки"
        "\n/inline_buttons - кнопки"
        "\n/kurs_valut - курс валют"
        "\n/counter - кликер")

    # await bot.send_message(chat_id= message.chat.id, text='Help message')

# ---Start---


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    for i in range(100):
        await message.answer("Hello World!")

# ---Roll---


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

# ---random_list---


def return_list(lists):
    a = str()
    for i in range(len(lists)):
        a += str(lists[i]).replace("[""]""'", "")
        if not i == (len(lists) - 1):
            a += ", "
    a += "."
    return a


@dp.message(Command("random_list"))
async def cmd_random_list(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        if len(args) == 3:
            random_list = [random.randint(int(args[0]), int(args[1])) for _ in range(int(args[2]))]
            await message.answer(
                f"Випадковий список від {args[0]} до {args[1]}, {args[2]} - символів: {return_list(random_list)}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

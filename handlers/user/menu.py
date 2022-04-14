from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Who are you?", reply_markup=menu)


@dp.message_handler(Text(equals=["Holerik", "Sangwinnik", "Flegmatic", "Melanholic"]))
async def gef_food(message: Message):
    await message.answer(f"You are {message.text}. Thanks", reply_markup=ReplyKeyboardRemove())
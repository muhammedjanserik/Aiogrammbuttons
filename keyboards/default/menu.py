from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Holerik")
        ],
        [
            KeyboardButton(text="Sangwinnik")
        ],
        [
            KeyboardButton(text="Flegmatic"),
            KeyboardButton(text="Melanholic")
        ]
    ],
    resize_keyboard=True
)
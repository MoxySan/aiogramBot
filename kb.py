from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = [
    [InlineKeyboardButton(text='Первая кнопка', callback_data='first_btn'),
    InlineKeyboardButton(text='Вторая кнопка', callback_data='second_btn'),
    ],
    [InlineKeyboardButton(text='Третья кнопка', callback_data='third_btn'),
    ],
    [InlineKeyboardButton(text='Четвертая кнопка', callback_data='chtvertay_btn')]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command
from kb import menu

router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет!')

@router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню:', reply_markup=menu)

@router.callback_query(F.data == 'second_btn')
async def second_btn_callback(сallback: types.CallbackQuery):
    await сallback.message.answer('Ты нажал на вторую кнопку')

@router.message(Command('adout'))
async def adout_cmd(message: types.Message):
    await message.answer('О нас:')

@router.message(F.text.lower().in_({'привет', 'здраствуй'}))
async def text_answer(message: types.Message):
    await message.answer('И тебе привет!')
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.admin_main_menu import admin_main_menu
from keyboards.default.user_main_menu import user_main_menu
from loader import dp, db_manager
from states.RegisterState import Register


@dp.message_handler(commands="help", state="*")
async def help_handler(message: types.Message, state: FSMContext):
    if db_manager.get_user(message):
        text = "Yordam\nBoglanish uchun:\nTel: +998 88 788 06 60\n😊"
        await message.answer(text=text, reply_markup=user_main_menu)
        await state.finish()
        
@dp.message_handler(commands="help", chat_id=ADMINS)
async def admin_help_handler(message: types.Message):
    text = "Yordam\nBoglanish uchun:\nTel: +998 88 788 06 60\n😊"
    await message.answer(text=text, reply_markup=admin_main_menu)
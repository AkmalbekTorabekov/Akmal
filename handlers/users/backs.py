from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_main_menu import admin_main_menu
from keyboards.default.user_main_menu import user_main_menu
from loader import dp


@dp.message_handler(text="⬅️ Orqaga", state="*")
async def stickers_menu(message: types.Message, state: FSMContext):
    text = "Bosh menyuga xush kelibsiz 😊"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()


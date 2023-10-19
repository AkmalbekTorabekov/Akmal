from aiogram import types

from keyboards.default.user_main_menu import user_main_menu
from loader import dp


@dp.message_handler(text="📞 Aloqa uchun")
async def start_handler(message: types.Message):
    text = "Biz bilan muloqotga chiqish uchun.\nTel: +998 88 788 06 60\nTelegram: @Akmalbek0660"
    await message.answer(text=text, reply_markup=user_main_menu)

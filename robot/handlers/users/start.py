from aiogram import types
from aiogram.dispatcher import FSMContext
# from keyboards.default.defoult_btn import menu_btn, phone_btn
from loader import dp, bot
from data.api import create_user, get_me


@dp.message_handler(CommandStart)
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
    user = await get_me(message.from_user.id)
    if user["status_code"] == 200:
        await message.answer(f"Sizga nima kerak?", reply_markup=menu_btn)
    else:
        await message.answer("Ro'yxatdan o'tish uchun Ismingizni kiriting: ", reply_markup=types.ReplyKeyboardRemove()  )
        await state.set_state("get_name")

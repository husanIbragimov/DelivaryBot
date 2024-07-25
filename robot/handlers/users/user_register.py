from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, Message

from data.api import get_me, register_user
from filters import IsPrivateChat
from utils.states import UserForm

router = Router()
router.message.filter(IsPrivateChat())


@router.message(CommandStart())
async def get_started(message: Message, state: FSMContext):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
    user = await get_me(message.from_user.id)
    if user['status_code'] == 200:
        await message.answer('Siz ro\'yxatdan o\'tdingiz!')
    else:
        await state.set_state(UserForm.name)
        await message.answer('Ismingizni kiriting: ', reply_markup=ReplyKeyboardRemove())


@router.message(UserForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserForm.phone_number)
    await message.answer('Telefon raqamingizni kiriting: ', reply_markup=ReplyKeyboardRemove())


@router.message(UserForm.phone_number)
async def get_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    print(data)
    await register_user(
        telegram_id=message.from_user.id,
        username=data['username'],
        nickname=data['full_name'],
        phone_number=data['phone_number']
    )
    await state.clear()

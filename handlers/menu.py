from aiogram import Router,F
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import CommandStart,Command
from aiogram.utils.markdown import hbold
from keyboards.menu import menu
from aiogram.fsm.context import FSMContext
from states.singup import Form

menu_router = Router = Router()

@menu_router.message(F.text=="Sherik kerak")
async def menu(message: Message):
    await message.answer("""Sherik topish uchun ariza berish\n

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")


@menu_router.message(Form.ism_familya)
async def user_neme(message: Message, state: FSMContext):
    await state.update_data(ism_familya=message.text)
    await state.set_state(Form.texnologiya)
    await message.answer('''📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''')
    

@menu_router.message(Form.texnologiya)
async def user_neme(message: Message, state: FSMContext):
    await state.update_data(texno=message.text)
    await state.set_state(Form.aloqa)
    await message.answer('''📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67''')
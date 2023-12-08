from aiogram import Router
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import CommandStart,Command
from aiogram.utils.markdown import hbold
from keyboards.menu import menu

start_router: Router = Router()

@start_router.message(Command("start"))
async def start_rauter(message: Message):
   
    await message.answer(f"""Assalom alaykum {hbold(message.from_user.full_name)}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling! """,reply_markup=menu)





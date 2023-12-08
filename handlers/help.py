from aiogram import Router
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import CommandStart,Command
from aiogram.utils.markdown import hbold


help_router: Router = Router()

@help_router.message(Command("help"))
async def help_dispecher(message: Message):
    await message.answer("""UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. \n

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. \n

E'lon berish: @UstozShogirdBot\n

Admin @UstozShogirdAdminBot \n""")
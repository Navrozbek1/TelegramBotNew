import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction

from app.keyboards import keyboard1

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(0.5)
    await message.answer(f"Assalomu alaykum hurmatli {message.from_user.full_name} botimizga xush kelibsiz!", reply_markup=keyboard1)
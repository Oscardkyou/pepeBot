from aiogram.types import Message
from aiogram import Router
from keyboards.keyboard import kb_builder


router = Router()


@router.message()
async def sedn_echo(message: Message):
   await message.send_copy(chat_id=message.chat.id)
   await message.answer(text='Вот клавиатура', reply_markup=kb_builder.as_markup(resize_keyboard=True))
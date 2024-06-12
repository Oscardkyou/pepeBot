from aiogram.types import Message
from aiogram import Router
from keyboards.keyboard import kb_builder


router = Router()


@router.message()
async def sedn_echo(message: Message):
   await message.send_copy(chat_id=message.chat.id)
   await message.answer(text='Вот клавиатура', reply_markup=kb_builder.as_markup(resize_keyboard=True))
   #допиши сюда код, который будет отправлять сообщение обратно пользователю
   #с клавиатурой kb_builder
   #подсказка: используй метод send_copy у объекта message
   #подсказка: используй метод answer у объекта message  
   #подсказка: используй параметр reply_markup у метода answer
   #подсказка: используй параметр as_markup у объекта kb_builder

   
   
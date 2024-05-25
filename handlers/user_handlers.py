from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon import LEXICON_RU, LEXICON_KEY
from keyboards.keyboard import create_start_keyboard, create_referal_keyboard
from aiogram import F, Router


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
   await message.answer(text=LEXICON_RU['/start'], reply_markup=create_start_keyboard().as_markup())



@router.message(Command(commands='help'))
async def process_help_command(message: Message):
   await message.answer(text=LEXICON_RU['/help'])


@router.message(F.text == LEXICON_KEY['info'])
async def get_info(message: Message):
   await message.answer(text=LEXICON_RU['info'], reply_markup=create_referal_keyboard(), parse_mode='MarkdownV2')


@router.message(F.text == LEXICON_KEY['referal'])
async def get_referal_link(message: Message):
   await message.answer(text=LEXICON_RU['referal'])


@router.message(F.text == LEXICON_KEY['wallet'])
async def get_wallet(message: Message):
   await message.answer(text=LEXICON_RU['wallet'])


@router.edited_message()
async def sedn_echo(message: Message):
   await message.send_copy(chat_id=message.chat.id)
   await message.answer(text='Вот клавиатура', reply_markup=create_start_keyboard().as_markup())

@router.message(F.text == LEXICON_KEY['menu'])
async def get_menu(message: Message):
   await message.answer(text=LEXICON_RU['menu'], reply_markup=create_start_keyboard().as_markup())


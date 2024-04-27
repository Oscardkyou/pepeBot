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


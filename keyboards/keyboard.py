from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_KEY

kb_builder = ReplyKeyboardBuilder()


def create_start_keyboard():
   kb_builder = ReplyKeyboardBuilder()
   buttons = [KeyboardButton(text=i) for i in LEXICON_KEY.values()]
   kb_builder.row(*buttons)
   return kb_builder


def create_referal_keyboard():
   url_button = InlineKeyboardButton(text='Пригласить друга', url='https://gitbook.tonraffles.org/ton-raffles/modules/jetton-launchpad/fairlaunch/how-to-create-a-fair-launch')
   keyboard = InlineKeyboardMarkup(inline_keyboard=[[url_button]])
   return keyboard
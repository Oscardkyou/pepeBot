from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


kb_builder = ReplyKeyboardBuilder()


buttons = [KeyboardButton(text=f"Кнопка {i+1}") for i in range(10)]


kb_builder.row(*buttons, width=2)

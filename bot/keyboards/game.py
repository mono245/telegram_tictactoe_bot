from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def game_kb(fields: list[str] = ["-"] * 9) -> InlineKeyboardMarkup:
   """
   returns inline keyboard in format:\n
   '-' '-' '-'\n
   '-' '-' '-'\n
   '-' '-' '-'

   :param fields: fields to fill
   :return:
   """

   builder = InlineKeyboardBuilder()

   for i in range(9):
      builder.button(text=fields[i], callback_data=f"field_{i}")
   builder.adjust(3)

   return builder.as_markup(resize_keyboard=True)

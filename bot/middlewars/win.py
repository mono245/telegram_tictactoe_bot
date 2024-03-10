from typing import Callable, Awaitable, Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ..utils import is_win
from ..keyboards import game_kb


class WinMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]], 
            event: CallbackQuery, 
            data: Dict[str, Any]
        ) -> Any:
        if not isinstance(event, CallbackQuery):
            return await handler(event, data)
        
        await handler(event, data)
        
        state: FSMContext = data["state"]
        fields_data = await state.get_data()

        try:
            fields = fields_data["fields"]
        except KeyError:  # if state is clear
            return

        if is_win(fields, "X"):  # player win
            await event.message.edit_text(
                "<b>Вы победили!</b>",
                reply_markup=game_kb(fields)
            )
            await state.clear()
            return
        
        if is_win(fields, "O"):  # bot win
            await event.message.edit_text(
                "<b>Вы проиграли!</b>",
                reply_markup=game_kb(fields)
            )
            await state.clear()
            return
        
        if "-" not in fields:  # tie
            await event.message.edit_text(
                "<b>Ничья!</b>",
                reply_markup=game_kb(fields)
            )
            await state.clear()
            return

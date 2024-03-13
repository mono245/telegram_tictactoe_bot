from typing import Callable, Awaitable, Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ..keyboards import game_kb


def _is_win(fields: list[str], char: str) -> bool:
    """
    checking if char param wins in tic-tac-toe
    
    :param char: character, X or O
    """
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    
    for condition in win_conditions:
        if all(fields[i] == char for i in condition):
            return True
    return False


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

        if _is_win(fields, "X"):  # player win
            await event.message.edit_text(
                "<b>Вы победили!</b>",
                reply_markup=game_kb(fields)
            )
            await state.clear()
            return
        
        if _is_win(fields, "O"):  # bot win
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

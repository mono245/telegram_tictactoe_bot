from random import choice

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ..keyboards import game_kb
from ..states import InGame
from ..middlewares import WinMiddleware


def _bot_choice(fields: list[str]) -> int:
    empty_fields = [i for i, field in enumerate(fields) if field == "-"]

    if not empty_fields:  # if there's no free fields
        return -1
    
    return choice(empty_fields)


router = Router()
router.callback_query.middleware(WinMiddleware())


@router.callback_query(
    InGame.in_game, F.data.startswith("field_")
)
async def fields_callback(callback: CallbackQuery, state: FSMContext) -> None:
    fields_data = await state.get_data()
    field_index = int(callback.data.split("_")[1])  # getting field number (0-8)
    fields: list[str] = fields_data["fields"]
    
    if fields[field_index] == "-":  # if field is free
        fields[field_index] = "X"  # user choice
        
        bc = _bot_choice(fields)
        if bc != -1:
            fields[bc] = "O"  # bot choice

        await state.update_data(fields=fields)

        await callback.message.edit_reply_markup(
            reply_markup=game_kb(fields)
        )

    await callback.answer()

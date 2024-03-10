from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from ..states import InGame
from ..keyboards import game_kb


router = Router()


@router.message(default_state, Command("play"))
async def cmd_play(message: Message, state: FSMContext) -> None:
    await state.update_data(fields=['-'] * 9)
    await message.answer(
        "Сделайте ход:",
        reply_markup=game_kb()
    )
    await state.set_state(InGame.in_game)

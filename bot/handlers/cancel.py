from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(default_state, Command("cancel"))
async def cancel_no_state(message: Message, state: FSMContext) -> None:
    await state.set_data({})
    await message.answer("Нечего отменять")


@router.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Игра отменена")
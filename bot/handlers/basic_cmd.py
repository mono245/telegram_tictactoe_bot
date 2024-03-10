from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import html


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!\n"
        "Отправь боту /play чтобы начать игру"
    )


@router.message(Command("src"))
async def cmd_src(message: Message) -> None:
    await message.answer(
        "Исходный код " 
        "<a href=\"https://github.com/mono245/telegram_tictactoe_bot\">здесь</a>"
    )

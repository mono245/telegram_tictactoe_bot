import asyncio
import logging
from os import getenv

from .handlers import callbacks, cancel, play, basic_cmd

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s |%(levelname)s| - %(name)s: %(message)s"
    )
    load_dotenv()

    default = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(getenv("BOT_TOKEN"), default=default)
    dp = Dispatcher()
    dp.include_routers(
        callbacks.router, cancel.router, play.router, basic_cmd.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

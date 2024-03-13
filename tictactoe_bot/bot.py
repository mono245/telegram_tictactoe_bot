import asyncio
import logging

from .handlers import callbacks, cancel, play, basic_cmd
from .data import config

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties


async def run() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s |%(levelname)s| - %(name)s: %(message)s"
    )

    default = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(config.BOT_TOKEN, default=default)
    dp = Dispatcher()
    dp.include_routers(
        callbacks.router, cancel.router, play.router, basic_cmd.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()

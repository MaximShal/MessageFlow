import asyncio

from mf_bot.telegram_bot import run_bot
from rabbitmq.listners import create_rabbitmq_listener


async def main() -> None:
    asyncio.create_task(run_bot())
    asyncio.create_task(create_rabbitmq_listener())

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())

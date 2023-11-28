import aio_pika
import logging
import requests

from settings import AMQP_CREDENTIALS, AMQP_QUEUE_NAME, EXTERNAL_API_URL
from mf_bot.telegram_bot import get_last_message, ALL_MESSAGES


async def create_rabbitmq_listener() -> None:
    connection = await aio_pika.connect_robust(**AMQP_CREDENTIALS)
    channel = await connection.channel()
    queue = await channel.declare_queue(AMQP_QUEUE_NAME)

    async def callback(message: aio_pika.IncomingMessage):
        async with message.process():
            command = message.body.decode()

            if command == 'print':
                msg = await get_last_message()
                await print_message(msg)
            elif command == 'print_all':
                await print_all_messages()
            elif command == 'send':
                await send_last_message()
            else:
                print(f'[DEBUG] Unknown command: {command}')

    await queue.consume(callback)
    logging.info('Waiting for messages.')


async def print_message(msg: dict) -> None:
    if msg:
        logging.info(f"\n*****{msg['chat_id']}*****\n{msg['username']}: {msg['message']}")


async def print_all_messages() -> None:
    for msg in ALL_MESSAGES:
        await print_message(msg)


async def send_last_message() -> None:
    msg = await get_last_message()
    if msg:
        response = requests.post(EXTERNAL_API_URL, data=msg)
        logging.info(f'Sent with status: {response.status_code}')

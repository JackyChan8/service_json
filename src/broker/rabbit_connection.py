import json
from dataclasses import dataclass
from aio_pika import connect_robust, Message
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

from src.logger import logger
from src.config import settings


CONNECTING = 'Connecting to the RabbitMQ...'
CONNECTED = 'Successfully connected to the RabbitMQ!'
NOT_CONNECTED = 'The message could not be sent because the connection with RabbitMQ is not established'


@dataclass
class RabbitConnection:
    connection: AbstractRobustConnection | None = None
    channel: AbstractRobustChannel | None = None

    def status(self) -> bool:
        """
            Checks if connection established
        """
        if self.connection.is_closed or self.channel.is_closed:
            return False
        return True

    async def _clear(self) -> None:
        """
            Clear Connection
        """
        if not self.channel.is_closed:
            await self.channel.close()
        if not self.connection.is_closed:
            await self.connection.close()

        self.connection = None
        self.channel = None

    async def connect(self) -> None:
        """
            Establish connection with the RabbitMQ
        """
        logger.info(CONNECTING)
        try:
            self.connection = await connect_robust(settings.build_rabbit_url())
            self.channel = await self.connection.channel(publisher_confirms=False)
            logger.info(CONNECTED)
        except Exception as e:
            await self._clear()
            logger.error(e.__dict__)

    async def disconnect(self) -> None:
        """
            Disconnect and clear connections from RabbitMQ
        """
        await self._clear()

    async def send_messages(self,
                            messages: list | dict,
                            routing_key: str = settings.RABBITMQ_QUEUE) -> None:
        """
            Public message or messages to the RabbitMQ queue.
        """
        if not self.channel:
            raise RuntimeError(NOT_CONNECTED)

        if isinstance(messages, dict):
            messages = [messages]

        async with self.channel.transaction():
            for message in messages:
                message = Message(
                    body=json.dumps(message).encode()
                )

                await self.channel.default_exchange.publish(
                    message, routing_key=routing_key,
                )


rabbit_connection = RabbitConnection()
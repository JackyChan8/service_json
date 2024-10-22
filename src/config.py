from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
        Settings Class
    """

    # Application
    APP_NAME: str
    APP_VERSION: str
    APP_SUMMARY: str
    APP_DESCRIPTION: str

    # RabbitMQ
    RABBITMQ_QUEUE: str
    RABBITMQ_LOCAL_PORT: int
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: SecretStr
    RABBITMQ_LOCAL_HOST_NAME: str

    # Postgres
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASS: SecretStr
    POSTGRES_NAME: str

    def build_postgres_url(self, protocol_db: str = 'postgresql+asyncpg') -> str:
        """
            Build Postgres URL
            :param protocol_db protocol database
            :return: str
        """
        return (f"{protocol_db}://"
                f"{self.POSTGRES_USER}:{self.POSTGRES_PASS.get_secret_value()}@"
                f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}")

    def build_rabbit_url(self):
        """
            Build Rabbit URL
        """
        return (f'amqp://'
                f'{self.RABBITMQ_DEFAULT_USER}:{self.RABBITMQ_DEFAULT_PASS.get_secret_value()}@'
                f'{self.RABBITMQ_LOCAL_HOST_NAME}:{self.RABBITMQ_LOCAL_PORT}/')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = AppSettings()

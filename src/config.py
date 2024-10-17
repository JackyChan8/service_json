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

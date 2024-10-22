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

    # Postgres
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASS: SecretStr
    POSTGRES_NAME: str

    # Postgres Test
    TEST_POSTGRES_HOST: str
    TEST_POSTGRES_PORT: int
    TEST_POSTGRES_USER: str
    TEST_POSTGRES_PASS: SecretStr
    TEST_POSTGRES_NAME: str

    def build_postgres_url(self, protocol_db: str = 'postgresql+asyncpg') -> str:
        """
            Build Postgres URL
            :param protocol_db protocol database
            :return: str
        """
        return (f"{protocol_db}://"
                f"{self.POSTGRES_USER}:{self.POSTGRES_PASS.get_secret_value()}@"
                f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}")

    def build_postgres_test_url(self, protocol_db: str = 'postgresql+asyncpg'):
        """
            Build Postgres test URL
        """
        return (f"{protocol_db}://"
                f"{self.TEST_POSTGRES_USER}:{self.TEST_POSTGRES_PASS.get_secret_value()}@"
                f"{self.TEST_POSTGRES_HOST}:{self.TEST_POSTGRES_PORT}/{self.TEST_POSTGRES_NAME}")

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = AppSettings()

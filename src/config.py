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

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = AppSettings()

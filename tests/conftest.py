import pytest
import asyncio
from httpx import AsyncClient
from typing import AsyncGenerator

from main import app
from src.config import settings


@pytest.fixture(scope="function")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

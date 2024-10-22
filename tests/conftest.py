import pytest
import asyncio

from httpx import AsyncClient
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from main import app
from src.models import Base
from src.config import settings
from src.database import get_async_session


# Create a test database engine
DATABASE_URL = settings.build_postgres_test_url()
engine = create_async_engine(DATABASE_URL, echo=False)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Dependency override to use the test database
async def override_get_async_session():
    async with async_session_maker() as session:
        yield session


@pytest.fixture(scope='function')
async def async_session():
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(scope="function")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="function", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

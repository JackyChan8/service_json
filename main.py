from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from src.logger import logger
from src.config import settings
from src.routers import retransmission_router
from src.broker.rabbit_connection import rabbit_connection


@asynccontextmanager
async def lifespan(application: FastAPI):
    logger.info("Application is Started")
    await rabbit_connection.connect()
    yield
    await rabbit_connection.disconnect()
    logger.info("Application is End")

app = FastAPI(
    docs_url='/swagger_docs',
    lifespan=lifespan,
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    summary=settings.APP_SUMMARY,
    description=settings.APP_DESCRIPTION,
)

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(retransmission_router)

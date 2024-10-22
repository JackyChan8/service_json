from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.logger import logger
from src.models import PortfolioV01
from src.routers.retransmission import schemas


# ================================================== Create
async def create_portfolio(data: schemas.PortfolioSchema, session: AsyncSession) -> bool:
    """
        Create Portfolio Service
    """
    try:
        query = (
            insert(PortfolioV01)
            .values(**data.model_dump())
        )
        await session.execute(query)
        await session.commit()
        return True
    except Exception as e:
        logger.error(f'Exception by create portfolio: {e}')
        return False

from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from src.routers.retransmission import (
    schemas as retransmission_schema,
    services as retransmission_service,
)
from src.database import get_async_session
from src.schemas import schemas as global_schemas
from src.exceptions import exceptions as global_exceptions


router = APIRouter(prefix='/retransmission', tags=['retransmission'])

@router.post(path='/send',
             description='Retransmission json',
             status_code=status.HTTP_200_OK,
             responses={})
async def retransmission_json(data: retransmission_schema.AnyJson, session: AsyncSession = Depends(get_async_session)):
    """
        Retransmission JSON
    """

    data_json = data.root
    data_schemas = retransmission_schema.PortfolioSchema(**data_json)

    # Create
    is_create = await retransmission_service.create_portfolio(data_schemas, session)

    if not is_create:
        raise global_exceptions.MyHTTPException(
            status=global_schemas.StatusResponseEnum.ERROR,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message='An error occurred while adding portfolio',
        )
    raise global_exceptions.MyHTTPException(
        status=global_schemas.StatusResponseEnum.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        message='Successfully added portfolio',
    )

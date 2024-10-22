from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from src.routers.retransmission import (
    schemas as retransmission_schema,
    services as retransmission_service,
)
from src.database import get_async_session
from src.schemas import schemas as global_schemas
from src.exceptions import exceptions as global_exceptions


router = APIRouter(prefix='/portfolio', tags=['portfolio'])

@router.post(path='/add',
             description='Add Portfolio',
             status_code=status.HTTP_201_CREATED,
             responses={
                 status.HTTP_201_CREATED: {
                     'description': 'Портфолио успешно добавлено',
                     'content': {
                         'application/json': {
                             'schema': {
                                 'type': 'object',
                                 'properties': {'detail': 'string'}
                             }
                         }
                     }
                 },
                 status.HTTP_500_INTERNAL_SERVER_ERROR: {
                     'description': 'Произошла ошибка при добавлении портфолио в БД',
                     'content': {
                         'application/json': {
                             'schema': {
                                 'type': 'object',
                                 'properties': {'detail': 'string'}
                             }
                         }
                     }
                 },
             })
async def add_portfolio(data: retransmission_schema.AnyJson, session: AsyncSession = Depends(get_async_session)):
    """
        Portfolio Add
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

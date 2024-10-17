from fastapi import APIRouter, status

from src.routers.retransmission import schemas
from src.broker.rabbit_connection import rabbit_connection


router = APIRouter(prefix='/retransmission', tags=['retransmission'])

@router.post(path='/send',
             description='Retransmission json',
             status_code=status.HTTP_200_OK,
             responses={})
async def retransmission_json(data: schemas.AnyJson):
    """
        Retransmission JSON
    """

    print('data: ', data)
    message = {
        'type': 'test_message',
        'message': 'Test message text'
    }
    await rabbit_connection.send_messages(messages=message)

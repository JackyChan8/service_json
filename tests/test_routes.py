import json
import pytest
import aiofiles

from fastapi import status


async def read_json_file(file_path: str):
    """
        Read JSON file
    """
    async with aiofiles.open(file_path, mode='r') as f:
        contents = await f.read()
        data = json.loads(contents)
    return data


@pytest.mark.asyncio
async def test_add_portfolio_success(async_client):
    """
        Test Add Portfolio Success
    """

    data_json = await read_json_file('tests/data_test.json')

    for data in data_json:

        response = await async_client.post('/portfolio/add', json=data)

        data = response.json()

        # Response Status
        assert response.status_code == status.HTTP_201_CREATED

        # Response Message
        assert data.get('detail') == 'Successfully added portfolio'

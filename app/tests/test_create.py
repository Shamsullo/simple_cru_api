import httpx
import pytest

from app.core.config import settings

BASE_URL = "http://localhost:8000"


@pytest.mark.asyncio
async def test_create_item_success():
    async with httpx.AsyncClient() as client:
        item_data = {"title": "New Item", "content": "This is a new item."}
        response = await client.post(
            f"{BASE_URL}/v1/items/", json=item_data,
            headers={"X-API-KEY": settings.api_key}
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["title"] == item_data["title"]
        assert response_data["content"] == item_data["content"]


@pytest.mark.asyncio
async def test_create_item_invalid_data():
    async with httpx.AsyncClient() as client:
        item_data = {"title": "", "content": 123}
        response = await client.post(f"{BASE_URL}/v1/items/", json=item_data,
                                     headers={"X-API-KEY": settings.api_key})
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_item_missing_fields():
    async with httpx.AsyncClient() as client:
        item_data = {"title": "New Item Without Content"}
        response = await client.post(f"{BASE_URL}/v1/items/", json=item_data,
                                     headers={"X-API-KEY": settings.api_key})
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_item_missing_api_key():
    async with httpx.AsyncClient() as client:
        item_data = {"title": "New Item", "content": "This is a new item."}
        response = await client.post(f"{BASE_URL}/v1/items/", json=item_data)
        assert response.status_code == 401

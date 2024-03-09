from fastapi import Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_401_UNAUTHORIZED

from app.core.config import settings

API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == settings.api_key:
        return api_key
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED
        )

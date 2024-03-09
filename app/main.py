from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from app.api.router import router as api_router

title = "Simple CRUD API"
description = "This API was built with FastAPI and provides simple CRUD " \
              "functionality of an item"
version = "1.0.0"

app = FastAPI(
    title=title,
    description=description,
    version=version,
    docs_url='/api/docs',
    redoc_url='/api/redocs',
)

get_openapi(
    title=title,
    description=description,
    version=version,
    routes=app.routes,
)

app.include_router(api_router, prefix="/v1")


@app.get("", include_in_schema=False)
async def health() -> JSONResponse:
    return JSONResponse(
        {"message": "It is working!"}
    )

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import crud, schemas
from app.core.auth import get_api_key
from app.core.database import get_db

router = APIRouter(prefix="/items", dependencies=[Depends(get_api_key)])


@router.post("/", response_model=schemas.ItemOut)
async def create_item(
        item: schemas.CreateItem, db_session: AsyncSession = Depends(get_db)
):
    """
    Create a new item in the database.

    Parameters:
    - item: schemas.CreateItem - The item details from the request body.
    - db_session: AsyncSession - Dependency that provides an asynchronous
    session to the database.

    Returns:
    - The created item, conforming to the schema defined in schemas.ItemOut.
    """
    return await crud.create_item(db_session, item)


@router.get("/", response_model=schemas.PaginatedItems)
async def read_items(
        page: int = 1,
        page_size: int = 10,
        db_session: AsyncSession = Depends(get_db)
):
    """
    Retrieve a paginated list of items from the database.

    Parameters:
    - page: int - The current page number for pagination.
    - page_size: int - The number of items to return per page.
    - db_session: AsyncSession - Dependency that provides an asynchronous
    session to the database.

    Returns:
    - A paginated list of items, according to the schema defined in
    schemas.PaginatedItems.
    """
    return await crud.read_items(db_session, page, page_size)


@router.put("/{item_id}", response_model=schemas.ItemOut)
async def update_item(
        item_id: int,
        item: schemas.UpdateItem,
        db_session: AsyncSession = Depends(get_db)
):
    """
    Update an existing item in the database.

    Parameters:
    - item_id: int - The ID of the item to update.
    - item: schemas.UpdateItem - The updated item details from the request body.
    - db_session: AsyncSession - Dependency that provides an asynchronous
    session to the database.

    Returns:
    - The updated item, conforming to the schema defined in schemas.ItemOut.

    Raises:
    - HTTPException: 404 - If no item with the given ID was found.
    """
    updated_item = await crud.update_item(db_session, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}")
async def delete_item(
        item_id: int, db_session: AsyncSession = Depends(get_db)
):
    """
    Delete an item from the database.

    Parameters:
    - item_id: int - The ID of the item to delete.
    - db_session: AsyncSession - Dependency that provides an asynchronous
    session to the database.

    Returns:
    - A confirmation message indicating the successful deletion.
    """
    return await crud.delete_item(db_session, item_id)

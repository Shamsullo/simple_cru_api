from fastapi import HTTPException
from sqlalchemy import func, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models import Item
from app.api.schemas import CreateItem, UpdateItem


async def create_item(db_session: AsyncSession, item: CreateItem):
    """
    Create a new item in the database.

    Parameters:
    - db_session (AsyncSession): The database session for executing queries.
    - item (CreateItem): The item data to create.

    Returns:
    - The created Item object.
    """
    item_obj = Item(title=item.title, content=item.content, status=item.status)
    db_session.add(item_obj)
    await db_session.commit()
    await db_session.refresh(item_obj)
    return item_obj


async def read_items(
        db_session: AsyncSession, page: int = 1, page_size: int = 10
):
    """
    Retrieve items from the database with pagination.

    Parameters:
    - db_session (AsyncSession): The database session for executing queries.
    - page (int): Current page number.
    - page_size (int): Number of items per page.

    Returns:
    - A dictionary containing the items and pagination details.
    """
    # Calculate the total number of items
    total_items_result = await db_session.execute(
        select(func.count()).select_from(Item)
    )
    total_items = total_items_result.scalar_one()

    # Calculate offset based on page number and size, then retrieve items
    offset_value = (page - 1) * page_size
    items_query = select(Item).offset(offset_value).limit(page_size)
    items_result = await db_session.execute(items_query)
    items = items_result.scalars().all()

    # Calculate total pages
    total_pages = (total_items + page_size - 1) // page_size

    return {
        "items": items,
        "total_items": total_items,
        "page": page,
        "total_pages": total_pages,
        "page_size": page_size,
    }


async def update_item(db_session: AsyncSession, item_id: int,
                      item_data: UpdateItem):
    """
    Update an existing item in the database.

    Parameters:
    - db_session (AsyncSession): The database session for executing queries.
    - item_id (int): The ID of the item to update.
    - item_data (UpdateItem): New data for updating the item.

    Returns:
    - The updated Item object, or None if not found.

    Raises:
    - NoResultFound: If no item with the provided ID was found.
    """
    try:
        query = (
            update(Item)
                .where(Item.id == item_id)
                .values(
                title=item_data.title,
                content=item_data.content,
                status=item_data.status
            )
                .returning(Item)
        )
        response = await db_session.execute(query)
        updated_item = response.scalars().one()
        await db_session.commit()
        return updated_item
    except NoResultFound:
        return None


async def delete_item(db_session: AsyncSession, item_id: int):
    """
    Delete an item from the database.

    Parameters:
    - db_session (AsyncSession): The database session for executing queries.
    - item_id (int): The ID of the item to delete.

    Returns:
    - The deleted Item object.

    Raises:
    - HTTPException: If no item with the provided ID was found.
    """
    item = await db_session.get(Item, item_id)
    if item:
        await db_session.delete(item)
        await db_session.commit()
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

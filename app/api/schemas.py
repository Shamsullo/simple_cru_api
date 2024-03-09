from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class StatusOptions(str, Enum):
    """
    Enumeration for item status options.

    Defines possible states of an item to maintain a controlled vocabulary for
    status fields.
    - active: Indicates the item is active and visible.
    - not_active: Indicates the item is not active or has been hidden.
    """
    active = 'active'
    not_active = 'not_active'


class CreateItem(BaseModel):
    """
    Schema for creating a new item.

    This model defines the data structure for creating a new item,
    including title, content, and status.
    The status defaults to 'active' if not specified.

    Attributes:
    - title (str): The title of the item.
    - content (str): The detailed content of the item.
    - status (StatusOptions): The status of the item, using predefined
    StatusOptions enumeration.
    """
    title: str
    content: str
    status: StatusOptions = StatusOptions.active


class ItemOut(BaseModel):
    """
    Schema for item output representation.

    This model is used to define the structure of an item when it is returned
    from the API. It includes an identifier and optionally includes content
     and status if available.

    Attributes:
    ...
    """
    id: int
    title: str
    content: Optional[str]
    status: Optional[StatusOptions]


class UpdateItem(BaseModel):
    """
    Schema for updating an existing item.

    This model allows for partial updates to an item, where any of the fields
    can be updated independently. All fields are optional, reflecting the
    ability to update any subset of the item's attributes.

    Attributes:
    - title (Optional[str]): The new title of the item, if updating.
    - content (Optional[str]): The new content of the item, if updating.
    - status (Optional[StatusOptions]): The new status of the item, if updating.
    """
    title: Optional[str]
    content: Optional[str]
    status: Optional[StatusOptions]


class PaginatedItems(BaseModel):
    """
    Schema for paginated item output.

    This model represents a page of items in a paginated response,
    including metadata about the pagination itself and the list of items.

    Attributes:
    - total_items (int): The total number of items across all pages.
    - total_pages (int): The total number of pages available.
    - page_size (int): The number of items per page.
    - items (List[ItemOut]): The list of items for the current page.
    """
    total_items: int
    total_pages: int
    page_size: int
    items: List[ItemOut]

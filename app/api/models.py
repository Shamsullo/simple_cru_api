from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Item(Base):
    """
    Item model for representing items in the database.
    """
    __tablename__ = "Item"

    id = Column(
        Integer, primary_key=True, comment="Unique identifier for each item"
    )
    title = Column(String, comment="Title of the item")
    content = Column(String, comment="Content or description of the item")
    status = Column(
        String, nullable=True,
        default="active",
        comment="Status of the item, defaults to 'active'"
    )

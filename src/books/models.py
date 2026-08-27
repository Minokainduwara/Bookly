from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid

class BookModel(SQLModel, table=True):
    __tablename__ = "books"

    uuid: uuid.UUID = Field( # type: ignore
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4()

        )
    )
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
    language: str
    created_at: datetime = Field(Column(pg.TIMESTAMP,default=datetime.now))
    updated_at: datetime = Field(Column(pg.TIMESTAMP,default=datetime.now))

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookModel, BookCreateModel, BookUpdateModel

class BookService:
    async def get_all_books(self, session: AsyncSession):
        pass

    async def get_book_by_id(self, book_uid: str, session: AsyncSession):
        pass

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        pass

    async def update_book(self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession):
        pass
    
    async def delete_book(self, book_uid: str, session: AsyncSession):
            pass


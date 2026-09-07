# API Endpoints
from fastapi import APIRouter,status, Depends
from typing import List
from fastapi.exceptions import HTTPException
#from src.books.book_data import books
from src.books.service import BookService
from src.books.schemas import BookModel,BookUpdateModel,BookCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()


# Get all books
@book_router.get("/",response_model=List[BookModel])
async def get_all_books(session:AsyncSession =Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

# Create a new book
@book_router.post("/",status_code=status.HTTP_201_CREATED, response_model=BookModel)
async def create_book(book_data:BookCreateModel,session:AsyncSession =Depends(get_session)) -> dict:
    new_book =await book_service.create_book(book_data,session)
    return new_book

# Get a book by ID
@book_router.get("/{book_uid}")
async def get_book_by_id(book_uid: int,session:AsyncSession =Depends(get_session)) -> dict:
    book = await book_service.get_book_by_id(book_uid,session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# Update a book by ID
@book_router.patch("/{book_uid}")
async def update_book_by_id(book_uid: int, book_update_data:BookUpdateModel,session:AsyncSession =Depends(get_session)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data,session)
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# Delete a book by ID
@book_router.delete("/{book_uid}")
async def delete_book_by_id(book_uid: int,session:AsyncSession =Depends(get_session)) -> dict:
    book_to_delete = await book_service.delete_book(book_uid,session)
    if book_to_delete:
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
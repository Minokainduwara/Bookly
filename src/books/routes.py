# API Endpoints
from fastapi import APIRouter,status
from typing import List
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import BookModel,BookUpdateModel

book_router = APIRouter()


# Get all books
@book_router.get("/",response_model=List[BookModel])
async def get_all_books():
    return books

# Create a new book
@book_router.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:BookModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

# Get a book by ID
@book_router.get("/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# Update a book by ID
@book_router.patch("/{book_id}")
async def update_book_by_id(book_id: int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# Delete a book by ID
@book_router.delete("/{book_id}")
async def delete_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
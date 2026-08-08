from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons",
        "publish_date": "1925-04-10",
        "page_count": 218,
        "language": "English",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "publish_date": "1960-07-11",
        "page_count": 281,
        "language": "English",
    },

    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "publish_date": "1949-06-08",
        "page_count": 328,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton, Whitehall",
        "publish_date": "1813-01-28",
        "page_count": 279,
        "language": "English",
    }
]

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

# Get all books
@app.get("/books",response_model=List[BookModel])
async def get_all_books():
    return books

# Create a new book
@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:BookModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

# Get a book by ID
@app.get("/book/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# Update a book by ID
@app.patch("/book/{book_id}")
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
@app.delete("/book/{book_id}")
async def delete_book_by_id(book_id: int, status_code=status.HTTP_204_NO_CONTENT):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
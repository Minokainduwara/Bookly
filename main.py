from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List


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

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
    language: str

@app.get("/books",response_model=List[Book])
async def get_all_books():
    return books

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/book/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    pass

@app.put("/book/{book_id}")
async def update_book_by_id(book_id: int) -> dict:
    pass

@app.delete("/book/{book_id}")
async def delete_book_by_id(book_id: int) -> dict:
    pass
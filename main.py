from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def read_root():
    return{"message": "Hello, World!"}

@app.get("/greet")
async def greet(name: Optional[str] = "User", age: int = 0) -> dict:
    # if name is "User":
    #     return {"message": "Hello, Guest!"}
    return {"message": f"Hello, {name}! You are {age}."}

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post("/create_book")
async def create_book(book: BookCreateModel):
    return{
        "title": book.title,
        "author": book.author
    }

@app.get("/get_headers",status_code=201)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent: Optional[str] = Header(None),
    Minoka:str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["mino"] = Minoka
    return request_headers
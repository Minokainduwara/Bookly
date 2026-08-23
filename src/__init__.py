#This mark src file as python package
#This Will be the entry point

from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    version=version
)

app.include_router(book_router, prefix="/api/{version}/books")
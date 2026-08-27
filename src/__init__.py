#This mark src file as python package
#This Will be the entry point

from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is Starting up...")
    yield
    print("Server is stopped...")
    

version = "v1"

app = FastAPI(
    title = "Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=lifespan
)

app.include_router(book_router, prefix="/api/{version}/books",tags=['books'])
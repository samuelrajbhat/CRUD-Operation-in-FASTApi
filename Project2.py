from typing import Optional
from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(title="Description of the book",
                                       max_length=100,
                                       min_length=1)

    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "Example": {
                'id': '4fa85f64-5717-4562-b3fc-2c963f66afa6',
                'title': 'Computer Science Pro',
                'Author': 'CodingWithRoby',
                'description': 'A Nice description of the book',
                'rating': 75
            }
        }


BOOKS = []


@app.get("/")
def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        crete_book_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in BOOKS:
        if x.id == book_id:
            counter += 1
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID: {book_id} deleted!!'


def crete_book_no_api():
    book1 = Book(id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 title="Title_1",
                 author="Author_1",
                 description="Description_1",
                 rating=60
                 )
    book2 = Book(id="2fa85f64-5717-4562-b3fc-2c963f66afa6",
                 title="Title_2",
                 author="Author_2",
                 description="Description_2",
                 rating=70
                 )
    book3 = Book(id="1fa85f64-5717-4562-b3fc-2c963f66afa6",
                 title="Title_3",
                 author="Author_3",
                 description="Description_3",
                 rating=80
                 )
    book4 = Book(id="0fa85f64-5717-4562-b3fc-2c963f66afa6",
                 title="Title_4",
                 author="Author_4",
                 description="Description_4",
                 rating=90)
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)

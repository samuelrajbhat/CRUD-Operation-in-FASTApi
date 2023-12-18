from fastapi import FastAPI
from typing import Optional

app = FastAPI()

BOOKS = {
        'Book_1': {'title': 'Title One', 'author': 'author One'},
        'Book_2': {'title': 'title Two', 'author': 'author Two'},
        'Book_3': {'title': 'title Three', 'author': 'author Three'},
        'Book_4': {'title': 'title Four', 'author': 'author Four'},
        'Book_5': {'title': 'title Five', 'author': 'author Five'}
}


@app.get("/")
async def read_all_books():
    return BOOKS


# path parameters adds additional variable to api calls

@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


# POST method

@app.post("/")
def create_book(boot_title, book_author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id + 1}'] = {'title': boot_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']


# PUT Method

@app.put("/{book_name}")
def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title,'author': book_author}
    BOOKS[book_name] = book_information
    return book_information


# QUERY Parameters

@app.get("/assignment/")
def read_book_assignment(book_name: str):
    return BOOKS[book_name]


@app.delete("/{book_name}")
def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'


# @app.get("/")
# async def skip_book_function(skip_book: Optional[str] = None):
#     if skip_book:
#         new_books = BOOKS.copy()
#         del new_books[skip_book]
#         return new_books
#     return BOOKS

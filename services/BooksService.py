from models.Book import Book
from flask import make_response

def add_book_service():
    return make_response({
        'status': 'success',
        'message': 'Hello Bookshelf API from database'
    })
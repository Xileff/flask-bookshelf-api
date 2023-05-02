from flask import Blueprint, request
from services.BooksService import *

book_route = Blueprint('book_route', __name__)

@book_route.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    return add_book_service(data)
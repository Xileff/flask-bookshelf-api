from flask import Blueprint, request
from services.BooksService import *

book_route = Blueprint('book_route', __name__)

@book_route.route('/', methods=['GET'])
def add_book():
    return add_book_service()
from flask import Blueprint, request, make_response
from exceptions.Client import ClientError
from services.BooksService import *

book_route = Blueprint('book_route', __name__)

@book_route.route('/books', methods=['POST'])
def add_book_handler():
    try:
        data = request.get_json()
        id = add_book(data)
        
        return make_response({
            'status': 'success',
            'message': 'Buku berhasil ditambahkan',
            'data': {
                'bookId': id,
                },
        }, 201)
    
    except ClientError as e:
        print(type(e))
        return make_response({
            'status': 'fail',
            'message': e.message,
        }, e.status_code)
    except Exception as e:
        return make_response({
            'status': 'fail',
            'message': str(e),
        }, 500)


@book_route.route('/books', methods=['GET'])
def get_books_handler():
    try:
        book_list = get_books()
        return make_response({
            'status': 'success',
            'data': {
                'books': book_list,
            },
        })
    except ClientError as e:
        print(type(e))
        return make_response({
            'status': 'fail',
            'message': e.message,
        }, e.status_code)
    except Exception as e:
        return make_response({
            'status': 'fail',
            'message': str(e),
        }, 500)

@book_route.route('/books/<string:id>', methods=['GET'])
def get_book_by_id_handler(id):
    try:
        book = get_book_by_id(id)

        return make_response({
            'status': 'success',
            'data': {
                'book': book,
            },
        })
    except ClientError as e:
        print(type(e))
        return make_response({
            'status': 'fail',
            'message': e.message,
        }, e.status_code)
    except Exception as e:
        return make_response({
            'status': 'fail',
            'message': str(e),
        }, 500)
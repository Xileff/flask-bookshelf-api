from flask import make_response
from nanoid import generate
from models.Book import Book
import datetime

def add_book_service(data):
    try:
        if 'name' not in data:
            return make_response({
                'status': 'fail',
                'message': 'Gagal menambahkan buku. Mohon isi nama buku'
            }, 400)
        
        name, year, author, summary, publisher, pageCount, readPage, reading = data.values()

        if readPage > pageCount:
            return make_response({
                'status': 'fail',
                'message': 'Gagal menambahkan buku. readPage tidak boleh lebih besar dari pageCount'
            }, 400)

        insertedAt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updatedAt = insertedAt
        id = generate(size=16)

        book = Book(
            id = id,
            name = name,
            year = year,
            author = author,
            summary = summary,
            publisher = publisher,
            page_count = pageCount,
            read_page = readPage,
            finished = pageCount == readPage,
            reading = reading,
            inserted_at = insertedAt,
            updated_at = updatedAt
        )

        book.save()

        return make_response({
            'status': 'success',
            'message': 'Buku berhasil ditambahkan',
            'data': {
                'bookId': id,
            }
        }, 201)

        
    except Exception as e:
        return make_response({
            'status': 'failed',
            'message': str(e)
        }, 500)

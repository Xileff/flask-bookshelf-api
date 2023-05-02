from nanoid import generate
from models.Book import Book
from errors.Client import ClientError
import datetime

def add_book(data):
    if 'name' not in data:
        raise ClientError('Gagal menambahkan buku. Mohon isi nama buku', 400)
    
    name, year, author, summary, publisher, pageCount, readPage, reading = data.values()

    if readPage > pageCount:
        raise ClientError('Gagal menambahkan buku. readPage tidak boleh lebih besar dari pageCount', 400)

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
    return id

def get_books():
    books = Book.query.all()
    book_list = [book.serialize_simple() for book in books]
    return book_list

def get_book_by_id(id):
    book = Book.query.filter_by(id=id).first()
    if not book:
        raise ClientError('Buku tidak ditemukan', 404)
    return book.serialize()
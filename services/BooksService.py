from nanoid import generate
from models.Book import Book
from errors.Client import ClientError
import datetime

def add_book(data: dict):
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

def get_books(name: str, reading: str, finished: str):
    query = Book.query # make a query object from Book model

    if name:
        query = query.filter(Book.name.ilike('%'+name+'%'))
    if reading is not None:
        query = query.filter_by(reading=bool(int(reading))) # convert the 'reading' query param data type to the matching data type in database(tinyint)
    if finished is not None:
        query = query.filter_by(finished=bool(int(finished)))
    
    books = query.all()
    book_list = [book.serialize_simple() for book in books]
    return book_list

def get_book_by_id(id: str):
    book = Book.query.filter_by(id=id).first()
    if not book:
        raise ClientError('Buku tidak ditemukan', 404)
    return book.serialize()

def update_book_by_id(id: str, data: dict):
    if 'name' not in data:
        raise ClientError('Gagal memperbarui buku. Mohon isi nama buku', 400)

    if data['readPage'] > data['pageCount']:
        raise ClientError('Gagal memperbarui buku. readPage tidak boleh lebih besar dari pageCount', 400)

    book = Book.query.filter_by(id=id).first()
    if not book:
        raise ClientError('Gagal memperbarui buku. Id tidak ditemukan', 404)
    
    book.update(data)

def delete_book_by_id(id: str):
    book = Book.query.filter_by(id=id).first()
    if not book:
        raise ClientError('Buku gagal dihapus. Id tidak ditemukan', 404)
    book.delete()
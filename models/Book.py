from database import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String, nullable=False)
    summary = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    pageCount = db.Column(db.Integer, nullable=False)
    readPage = db.Column(db.Integer, nullable=False)
    reading = db.Column(db.Boolean, nullable=False)
    insertedAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
from database import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String, nullable=False)
    summary = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    page_count = db.Column(db.Integer, nullable=False)
    read_page = db.Column(db.Integer, nullable=False)
    finished = db.Column(db.Boolean, nullable=False)
    reading = db.Column(db.Boolean, nullable=False)
    inserted_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Book %r>' & self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'author': self.author,
            'summary': self.summary,
            'publisher': self.publisher,
            'pageCount': self.page_count,
            'readPage': self.read_page,
            'finished': bool(self.finished),
            'reading': bool(self.reading),
            'insertedAt': self.inserted_at,
            'updatedAt': self.updated_at,
        }
    
    def serialize_simple(self):
        return {
            'id': self.id,
            'name': self.name,
            'publisher': self.publisher,
        }
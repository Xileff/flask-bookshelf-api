# Dependencies
from flask import Flask
from flask_cors import CORS
from config import Config
from database import db

# Blueprints(endpoint routes)
from api.books import book_route

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

CORS(app)

app.register_blueprint(book_route)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
# Dependencies
from flask import Flask, make_response
from flask_cors import CORS
from config import Config
from database import db
from api.books import book_route
from errors.Client import ClientError
import logging

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

CORS(app)

app.register_blueprint(book_route)

@app.errorhandler(ClientError)
def handle_client_error(e: ClientError):
    return make_response({
        'status': 'fail',
        'message': e.message,
    }, e.status_code)

logging.basicConfig(level=logging.ERROR)
@app.errorhandler(Exception)
def handle_server_error(e: Exception):
    logging.error(str(e), exc_info=True)
    return make_response({
        'status': 'fail',
        'message': 'Oops, sorry. Something went wrong on our side.',
    }, 500)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
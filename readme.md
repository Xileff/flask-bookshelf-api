# Flask Bookshelf API

<p align="center">
  <img src="https://flask.palletsprojects.com/en/2.1.x/_static/flask-icon.png" alt="Flask">
</p>


This is a project that I created to familiarize myself in using Flask to build RESTful API. It allows user to post books, search for books with or without certain filter, edit a book, and delete a book.

## Steps to run this project

1. Clone the repository: 
    ```bash
    git clone https://github.com/Xileff/flask-bookshelf-api.git
    ```

2. Move to the project folder, then make a virtual environment : 
    ```bash
    cd flask-bookshelf-api
    python -m venv venv
    ```

3. Activate the virtual environment(Windows) :
      ```bash
      For Windows : /venv/Scripts/activate

      For UNIX : source /venv/bin/activate
      ```

4. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

5. Make a .env file containing your MySQL database information :
    ```bash
    DB_HOST=<your_db_host>
    DB_USER=<your_db_username>
    DB_PASSWORD=<your_db_password>
    DB_NAME=try_flask
    ```

6. Import the database from *try_flask.sql* file to your MySQL

7. Import the Postman tests collection and environment from the folder *postman*

8. Start the app
    ```bash
    python app.py
    ```

9. Run the Postman collection to test the application
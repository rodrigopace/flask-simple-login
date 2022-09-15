### Install the requirements

*   pip install -r requirements

Make sure to adjust the environment variable on `.flaskenv`

### Initialize the DB

You can use any other DB like MySQL or SQLite

* flask db init
* flask db migrate -m "Initial migration."
* flask db upgrade

### Start the app

* flask run
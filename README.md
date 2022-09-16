### Install the requirements

*   pip install -r requirements

Make sure to adjust the environment variable on `.flaskenv`

### Initialize the DB

You can use any other DB like MySQL or SQLite

* flask db init
* flask db migrate -m "Initial migration."
* flask db upgrade

### Start the app at 5000/TCP

* flask run

To run flask on your local IP (not localhost), run:

* flask run --host=0.0.0.0

Notes:

1. **DO NOT** run this app in a production environment.
2. This app must be used for educational purposes only.
3. Make sure to open the correct ports in your perimeter security.
4. Make sure to close all accesses after using this app
5. Make sure to open ports on your host firewall
6. Make sure your SE-Linux allows connections to your server
7. **THIS LAB MUST NOT BE USED IN A PRODUCTION ENVIRONMENT**

import logging
from flask import Blueprint


mod_app = Blueprint('app', __name__)

@app.route('/')
def hello():
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
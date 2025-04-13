"""Module providing Flask functionality."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    This is a hello world function

    Returns
    -------
    Hello world html text
    """
    return "<p>Hello, World!</p>"
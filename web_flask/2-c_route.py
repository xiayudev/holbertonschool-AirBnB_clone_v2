#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """HBNB page"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")

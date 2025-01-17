#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask, abort, render_template

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
    """C page"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text=None):
    """Python page"""
    return "Python {}".format(text.replace("_", " ") if text else "is cool")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Number page"""
    if type(n) is int:
        return "{} is a number".format(n)
    abort(404)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Number Template page"""
    if type(n) is int:
        return render_template("5-number.html", n=n)
    abort(404)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Number Odd Or Even page"""
    if type(n) is int:
        return render_template("6-number_odd_or_even.html", n=n)
    abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

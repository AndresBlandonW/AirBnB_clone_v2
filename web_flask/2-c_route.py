#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """route index"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "route hbnb"
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cfun(text):
    "route C"
    new_t = text.replace('_', ' ')
    return "C " + new_t


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
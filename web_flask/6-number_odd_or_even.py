#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

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


@app.route('/python', defaults={'text': None}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonr(text):
    "route python"
    if text is None:
        return "Python is cool"

    newt = text.replace('_', ' ')
    return "Python " + newt


@app.route("/number/<int:n>", strict_slashes=False)
def numberr(n):
    "route number"
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """route template"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """router number is odd or even"""
    if type(n) is int:
        if n % 2 == 0:
            check = 'even'
        else:
            check = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, check=check)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

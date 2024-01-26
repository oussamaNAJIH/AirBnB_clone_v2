#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    displays hello HBNB
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    displays HBNB
    """
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    display “C ” followed by the value of the text variable
    """
    return f"C {escape(text)}".replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

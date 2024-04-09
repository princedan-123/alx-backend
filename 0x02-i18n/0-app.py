#!/usr/bin/env python3
"""A simple flask app."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """A route to the homepage of the application."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

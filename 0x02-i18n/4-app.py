#!/usr/bin/env python3
"""A simple flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

def get_locale():
    """A selector function that determines the users locale per request."""
    locale = request.args.get('locale', None)
    languages = app.config['LANGUAGES']
    if locale is not None and locale in languages:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
babel = Babel(app, locale_selector=get_locale)


class Config:
    """Default configuration setup for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

@app.route('/')
def home():
    """A route to the homepage of the application."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)

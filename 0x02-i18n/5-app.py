#!/usr/bin/env python3
"""A simple flask app."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import typing

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> typing.Union[typing.Dict, None]:
    """
        A functionrthat returns a user dictionary or None from
        the users dataset.
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None:
        return users.get(user_id)
    return user_id
@app.before_request
def before_request():
    """A function executed before every request handling."""
    user = get_user()
    if user is not None:
        g.user = user

class Config:
    """Default configuration setup for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """A selector function that determines the users locale per request."""
    locale = request.args.get('locale', None)
    languages = app.config.get('LANGUAGES')
    if locale is not None and locale in languages:
        return locale
    return request.accept_languages.best_match(app.config.get('LANGUAGES'))


@app.route('/')
def home():
    """A route to the homepage of the application."""
    return render_template('5-index.html', g=g)


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3
"""Basic Flask app module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config app class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


@app.route('/')
def index() -> str:
    """Index page"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """Get locale language"""
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """Returns a user dictionary or None if the ID cannot be found"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    else:
        return None


@app.before_request
def before_request():
    """Function to execute before each request"""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

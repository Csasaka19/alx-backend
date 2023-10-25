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


@app.route('/')
def index() -> str:
    """Index page"""
    return render_template('0-index.html')


@babel.localeselector
def get_locale() -> str:
    """Get locale language"""
    if request.args.get('locale'):
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

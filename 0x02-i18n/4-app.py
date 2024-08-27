#!/usr/bin/env python3
"""
Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header.
Create a babel.cfg file containing
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get the user's prefered languagge"""
    lang = request.args.get("locale")
    if lang in Config.LANGUAGES:
        return lang
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def index() -> str:
    """the index controller, returns the index.html"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)

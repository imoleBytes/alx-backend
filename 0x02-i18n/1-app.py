#!/usr/bin/env python3
"""
Install the Babel Flask extension:
Then instantiate the Babel object in your app. Store it in a
module-level variable named babel.
In order to configure available languages in our app, you will
 create a Config class that has a LANGUAGES class attribute
   equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en") and timezone ("UTC").
Use that class as config for your Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

babel = Babel(app)


@app.get('/', strict_slashes=False)
def index() -> str:
    """the index controller, returns the index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)

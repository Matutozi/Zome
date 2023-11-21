from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv
from urllib.parse import quote_plus
from zome.config import Config

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt(app)

app.config.from_object(Config)

db.init_app(app)


if app:
    from zome import routes

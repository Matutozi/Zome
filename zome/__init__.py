from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from urllib.parse import quote_plus


app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{getenv('MYSQL_USER')}:{quote_plus(getenv('MYSQL_PWD'))}@{getenv('MYSQL_HOST')}/{getenv('MYSQL_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


if app:
    from zome import routes

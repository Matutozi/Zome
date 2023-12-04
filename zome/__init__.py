from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from zome.config import Config

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt(app)

app.config.from_object(Config)
app.url_map.strict_slashes = False
db.init_app(app)


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error handler"""
    return jsonify({"error": "Not found"}), 404


if app:
    from zome import routes
    from zome.views import api

    app.register_blueprint(api)

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from zome.config import Config
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt(app)

app.config.from_object(Config)
app.url_map.strict_slashes = False
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error handler"""
    return render_template('error_404.html', title='Not Found'), 404


if app:
    from zome import routes
    from zome.views import api

    app.register_blueprint(api)

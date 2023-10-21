from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import cfg
from models import Staff, Event_to_telebot, Tasks

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
def create_app():
    app.config.update(**cfg)
    app.secret_key['SECRET_KEY'] = 'TEMPORARY_KEY'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    CORS(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
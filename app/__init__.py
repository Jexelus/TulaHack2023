from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import cfg
from flask_session import Session

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def create_app():
    app.config.update(**cfg)
    app.config['SECRET_KEY'] = 'TEMPORARY_KEY'
    app.config['SESSION_TYPE'] = 'filesystem'
    from app.models import User, Event_to_telebot, Tasks
    db.init_app(app)
    with app.app_context():
        db.create_all()
    CORS(app)
    Session(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login_get'

    @login_manager.user_loader
    def load_user(id_):
        print(User.query.get(int(id_)))
        return User.query.get(int(id_))

    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
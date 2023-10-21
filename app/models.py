from app import db
from flask_login import UserMixin


class Staff(db.Model, UserMixin):
    __tablename__ = 'Staff'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    login = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    telegram = db.Column(db.String(128))

class Event_to_telebot(db.Model):
    __tablename__ = 'Events_telebot'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    event_body = db.Column(db.String(256), primary_key=True)
    data = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    to = db.Column(db.Text, nullable=False)

class Tasks(db.Model):
    __tablename__ = 'Tasks'
    task_header = db.Column(db.Text, nullable=False)
    task_body = db.Column(db.Text, nullable=False)
    task_group = db.Column(db.Text, nullable=False)

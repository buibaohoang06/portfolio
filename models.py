from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import app

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    hashed_password = db.Column(db.String(), unique=False, nullable=False)
    user_id = db.Column(db.String(), unique=False, nullable=True)

class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    post_id = db.Column(db.String(), unique=True, nullable=False)
    post_title = db.Column(db.String(), unique=True, nullable=False)
    post_content=db.Column(db.String(), unique=False, nullable=False)
    post_thumbnail = db.Column(db.String(), unique=False, nullable=False, default="https://images.unsplash.com/photo-1600170034575-a55eba731232?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80")

class Achievements(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    achievement_id = db.Column(db.String(), unique=True, nullable=False)
    achievement_title = db.Column(db.String(), unique=True, nullable=False)
    achievement_date = db.Column(db.String(), unique=False, nullable=False)
    achievement_description = db.Column(db.String(), unique=False, nullable=False)
    achievement_link = db.Column(db.String(), unique=True, nullable=False)

    



from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(1000))
    date=db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    notes= db.relationship('Note')


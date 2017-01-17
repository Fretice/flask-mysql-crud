from datetime import datetime
from . import db


class Person(db.Model):
    __tables__ = "person"
    p_id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    location = db.Column(db.Text)
    comment = db.Column(db.Text)
    modifiedDate = db.Column(db.DateTime, default=datetime.utcnow)

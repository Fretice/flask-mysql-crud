from datetime import datetime
from . import db


class Person(db.Model):
    __tables__ = "Person"
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    location = db.Column(db.Text)
    comment = db.Column(db.Text)
    modifiedDate = db.Column(db.DateTime, default=datetime.utcnow)

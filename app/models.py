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

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        import random
        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            p = Person(name=forgery_py.name.full_name(),
                       gender=random.randint(0, 1),
                       age=random.randint(0, 100),
                       birthday=forgery_py.date.date(),
                       location=forgery_py.address.city(),
                       comment=forgery_py.currency.description(),
                       modifiedDate=datetime.utcnow())
            db.session.add(p)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
 
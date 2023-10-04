from app import db

class User(db.Model):
    username = db.Column(db.String(256), primary_key=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

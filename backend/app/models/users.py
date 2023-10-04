from app import db

class User(db.Model):
    userName = db.Column(db.String(120), primary_key=True)

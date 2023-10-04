from app import db

class Building(db.Model):
    name = db.Column(db.String(256), primary_key=True)
    bathrooms = db.relationship('Bathroom', backref='building', lazy=True)

from app import db

class Building(db.Model):
    name = db.Column(db.String(256), primary_key=True)

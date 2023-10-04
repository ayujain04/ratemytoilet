from app import db

class Location(db.Model):
    building = db.Column(db.String(120), primary_key=True)

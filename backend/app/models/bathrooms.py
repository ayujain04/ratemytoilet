from app import db

class Bathroom(db.Model):
    floor = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50), primary_key=True)
    location_building = db.Column(db.String(120), db.ForeignKey('location.building'))

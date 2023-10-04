from app import db

class Bathroom(db.Model):
    bn = db.Column(db.String(256), db.ForeignKey('building.name'), primary_key=True)
    floor = db.Column(db.String(128), primary_key=True)
    gender = db.Column(db.String(20), primary_key=True)
    
    # Relationship
    building = db.relationship('Building', backref=db.backref('bathrooms', lazy=True))

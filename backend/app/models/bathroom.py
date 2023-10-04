from app import db
from sqlalchemy import event
from sqlalchemy.orm import validates

class Bathroom(db.Model):
    bn = db.Column(db.String(256), db.ForeignKey('building.name'), primary_key=True)
    floor = db.Column(db.String(128), primary_key=True)
    gender = db.Column(db.String(20), primary_key=True)
    
    # Relationship
    building = db.relationship('Building', backref=db.backref('bathrooms', lazy=True))

    @validates('gender')
    def validate_gender(self, key, value):
        allowed_genders = ["Male", "Female", "Gender Neutral"]
        if value not in allowed_genders:
            raise ValueError(f"Gender must be one of {', '.join(allowed_genders)}")
        return value

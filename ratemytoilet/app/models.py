from app import db

class User(db.Model):
    userName = db.Column(db.String(80), primary_key=True)

class Location(db.Model):
    building = db.Column(db.String(80), primary_key=True)

class Bathroom(db.Model):
    floor = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10), primary_key=True)
    building = db.Column(db.String(80), db.ForeignKey('location.building'), nullable=False)

class Review(db.Model):
    reviewID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    additional_comments = db.Column(db.Text)
    overall_rating = db.Column(db.Integer)
    cryability = db.Column(db.Integer)
    cleanliness = db.Column(db.Integer)
    poopability = db.Column(db.Integer)
    userName = db.Column(db.String(80), db.ForeignKey('user.userName'), nullable=False)
    bathroom_floor = db.Column(db.Integer, db.ForeignKey('bathroom.floor'), nullable=False)
    bathroom_gender = db.Column(db.String(10), db.ForeignKey('bathroom.gender'), nullable=False)

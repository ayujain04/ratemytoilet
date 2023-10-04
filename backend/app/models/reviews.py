from app import db

class Review(db.Model):
    reviewID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    additional_comments = db.Column(db.Text)
    overall_rating = db.Column(db.Integer)
    cryability = db.Column(db.Integer)
    cleanliness = db.Column(db.Integer)
    poopability = db.Column(db.Integer)
    bathroom_floor = db.Column(db.Integer, db.ForeignKey('bathroom.floor'))
    bathroom_gender = db.Column(db.String(50), db.ForeignKey('bathroom.gender'))

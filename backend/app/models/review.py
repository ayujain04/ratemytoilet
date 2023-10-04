from app import db

class Review(db.Model):
    reviewid = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(256), db.ForeignKey('user.username'), nullable=False)
    poopability = db.Column(db.Integer, nullable=False)
    cleanliness = db.Column(db.Integer, nullable=False)
    cryability = db.Column(db.Integer, nullable=False)
    overall = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(256))

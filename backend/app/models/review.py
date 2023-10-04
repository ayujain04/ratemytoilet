from app import db

class Review(db.Model):
    reviewid = db.Column(db.Integer, primary_key=True)
    poopability = db.Column(db.Integer, nullable=False)
    cleanliness = db.Column(db.Integer, nullable=False)
    cryability = db.Column(db.Integer, nullable=False)
    overall = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(256))
    user = db.Columbn(db.String(256))

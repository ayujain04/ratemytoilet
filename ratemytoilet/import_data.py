import sys
import pandas as pd
from sqlalchemy.exc import IntegrityError

# Adjust the path to include your Flask app directory
sys.path.append("ratemytoilet/app")  # As per your provided path

from models import User, Location, Bathroom, Review
from app import app, db

def insert_data(row):
    try:
        # Check and insert user
        user = User.query.filter_by(userName=row["Username (you don't have to say ur actual name)"]).first()
        if not user:
            user = User(userName=row["Username (you don't have to say ur actual name)"])
            db.session.add(user)
        
        # Check and insert location (building)
        location = Location.query.filter_by(building=row["Building Name"]).first()
        if not location:
            location = Location(building=row["Building Name"])
            db.session.add(location)
        
        # Check and insert bathroom
        bathroom = Bathroom.query.filter_by(building=row["Building Name"], floor=row["Floor Number"], gender=row["Gender"]).first()
        if not bathroom:
            bathroom = Bathroom(floor=row["Floor Number"], gender=row["Gender"], building=row["Building Name"])
            db.session.add(bathroom)
        
        # Insert review
        review = Review(
            userName=row["Username (you don't have to say ur actual name)"],
            bathroom_floor=row["Floor Number"],
            bathroom_gender=row["Gender"],
            cleanliness=row["Cleanliness"],
            poopability=row["Poopability"],
            cryability=row["Cryability"],
            overall_rating=row["Overall Rating"],
            additional_comments=row.get("Additional Comments? ", None)  # Some comments might be NaN/missing
        )
        db.session.add(review)

        # Commit to the database
        db.session.commit()

    except IntegrityError:  # Handle any database constraints, like unique constraints
        db.session.rollback()

if __name__ == "__main__":
    # Load the CSV file into a DataFrame
    data = pd.read_csv('ratemytoilet/app/datadata.csv')  # As per your provided path
    
    # Push an application context
    with app.app_context():
        # Iterate over each row in the CSV and insert data
        data.apply(insert_data, axis=1)
        print("Data import completed!")
